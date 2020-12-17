day = '17'

with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
  content = f.read().strip().split('\n')


def skopiraj(dic):
  return {k:v for k, v in dic.items()}

def count_lit(grid):
  return sum(v for v in grid.values() if v)


##############################
##########  PART 1  ##########
##############################

def get_empty_grid1(m): # m = number of cycles
  '''
  cycle 0:   8 x 8 x 1
      x, y od 0 do 7, z = 0
  cycle 1:  10 x 10 x 3
      x, y od -1 do 8, z od -1 do 1

  ...

  cycle m: 8+2*m x 8+2*m x 1+2*m
      x, y od -m do 7+m, z od -m do m
  '''

  grid = {}
  for i in range(-m, 7+m+1):
    for j in range(-m, 7+m+1):
      for k in range(-m, m+1):
        grid[(i, j, k)] = False
  return grid

def initial_state1(grid): # uses .in data
  for i, row in enumerate(content):
    for j, cube in enumerate(row):
      if cube == '#':
        grid[(i, j, 0)] = True
  return grid

def make_cycle1(grid):
  old_grid = skopiraj(grid)
  for (x, y, z) in old_grid:
    active = 0

    # preštevamo aktivne sosede
    for x1 in range(max(-6, x-1), min(14, x+2)):
      for y1 in range(max(-6, y-1), min(14, y+2)):
        for z1 in range(max(-6, z-1), min(7, z+2)):
          if old_grid[(x1, y1, z1)] and (x, y, z) != (x1, y1, z1):
            active += 1

    if (old_grid[(x, y, z)] == True) and (active not in {2, 3}):
      grid[(x, y, z)] = False
    elif (old_grid[(x, y, z)] == False) and (active == 3):
      grid[(x, y, z)] = True

  return grid

def part1(cycles=6): # Day 17, part 1: 338 in 472ms
  empty_grid = get_empty_grid1(cycles)
  grid = initial_state1(empty_grid)
  for _ in range(cycles):
    grid = make_cycle1(grid)
  return count_lit(grid)


##############################
##########  PART 2  ##########
##############################

def get_empty_grid2(m): # m = number of cycles
  '''
  cycle 0:   8 x 8 x 1 x 1
      x, y od 0 do 7, z, w = 0
  cycle 1:  10 x 10 x 3 x 3
      x, y od -1 do 8, z, w od -1 do 1

  ...

  cycle m: 8+2*m x 8+2*m x 1+2*m x 1+2*m
      x, y od -m do 7+m, z, w od -m do m
  '''
  grid = {}
  for i in range(-m, 7+m+1):
    for j in range(-m, 7+m+1):
      for k in range(-m, m+1):
        for w in range(-m, m+1):
          grid[(i, j, k, w)] = False
  return grid

def initial_state2(grid): # uses .in data
  for i, row in enumerate(content):
    for j, cube in enumerate(row):
      if cube == '#':
        grid[(i, j, 0, 0)] = True
  return grid

def make_cycle2(grid):
  old_grid = skopiraj(grid)
  for (x, y, z, w) in old_grid:
    active = 0

    # preštevamo aktivne sosede
    for x1 in range(max(-6, x-1), min(14, x+2)):
      for y1 in range(max(-6, y-1), min(14, y+2)):
        for z1 in range(max(-6, z-1), min(7, z+2)):
          for w1 in range(max(-6, w-1), min(7, w+2)):
            if old_grid[(x1, y1, z1, w1)] and (x, y, z, w) != (x1, y1, z1, w1):
              active += 1

    if (old_grid[(x, y, z, w)] == True) and (active not in {2, 3}):
      grid[(x, y, z, w)] = False
    elif (old_grid[(x, y, z, w)] == False) and (active == 3):
      grid[(x, y, z, w)] = True

  return grid

def part2(cycles=6): # Day 17, part 2: 2440 in 19753ms
  empty_grid = get_empty_grid2(cycles)
  grid = initial_state2(empty_grid)
  for _ in range(cycles):
    grid = make_cycle2(grid)
  return count_lit(grid)


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

# Day 17, part 1: 338 in 458ms
# Day 17, part 2: 2440 in 19753ms