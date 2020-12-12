day = '12'

with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
  content = f.read().strip().split('\n')

content = [(row[0], int(row[1:])) for row in content]


##############################
##########  PART 1  ##########
##############################

def part1():
  dirs = ('E', 'N', 'W', 'S')
  cur_dir = 0 # direction bo vedno dirs[cur_dir % 4]
  position = [0, 0] # tuple ne dovoli item assigmenta, bi pa moral tuki neki drugega vpeljat.. oh well

  for d in content:
    if d[0] == 'E':
      position[0] += d[1]
    elif d[0] == 'N':
      position[1] += d[1]
    elif d[0] == 'W':
      position[0] -= d[1]
    elif d[0] == 'S':
      position[1] -= d[1]
    elif d[0] == 'L':
      cur_dir += (d[1] // 90)
      cur_dir = cur_dir % 4
    elif d[0] == 'R':
      cur_dir -= (d[1] // 90)
      cur_dir = cur_dir % 4
    elif d[0] == 'F':
      if dirs[cur_dir] == 'E':
        position[0] += d[1]
      elif dirs[cur_dir] == 'N':
        position[1] += d[1]
      elif dirs[cur_dir] == 'W':
        position[0] -= d[1]
      elif dirs[cur_dir] == 'S':
        position[1] -= d[1]
  
  return abs(position[0]) + abs(position[1])


##############################
##########  PART 2  ##########
##############################

def part2():
  wp = [10, 1] # waypoint
  position = [0, 0]

  for d in content:
    if d[0] == 'N':
      wp[1] += d[1]
    elif d[0] == 'S':
      wp[1] -= d[1]
    elif d[0] == 'W':
      wp[0] -= d[1]
    elif d[0] == 'E':
      wp[0] += d[1]
    
    elif d[0] == 'F':
      position[0] += (d[1] * wp[0])
      position[1] += (d[1] * wp[1])

    elif d[0] == 'L':
      for _ in range(d[1]//90):
        x, y = wp # python lol
        wp = [-y, x]
    elif d[0] == 'R':
      for _ in range(d[1]//90):
        x, y = wp # python lol
        wp = [y, -x]

  return abs(position[0]) + abs(position[1])


##############################
############ MAIN ############
##############################

import time

def main(redo_first=True, redo_second=True):
  if redo_first:
    start1 = time.time()
    r1 = part1()
    end1 = time.time()
    time1 = int(1000 * (end1 - start1))
    print(f'Day {day}, part 1: {r1} in {time1}ms')
    with open(f'2020/out/day_{day}_1.out', 'w', encoding='utf-8') as f:
      f.write(str(r1))

  if redo_second:
    start2 = time.time()
    r2 = part2()
    end2 = time.time()
    time2 = int(1000 * (end2 - start2))
    print(f'Day {day}, part 2: {r2} in {time2}ms')
    with open(f'2020/out/day_{day}_2.out', 'w', encoding='utf-8') as f:
      f.write(str(r2))

main()