day = '13'

with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
  content = f.read().strip().split('\n')


##############################
##########  PART 1  ##########
##############################
import itertools

def part1():
  TS = int(content[0]) # timestamp
  buses = [int(time) for time in content[1].split(',') if time != 'x']
  out = False
  for cur_time in itertools.count(TS):
    for bus_time in buses:
      if not cur_time % bus_time:
        ok_bus, departure_time, out = bus_time, cur_time, True
    if out:
      break
  return ok_bus * (departure_time - TS)


##############################
##########  PART 2  ##########
##############################

# Brez tega izreka ne bi šlo nikamor:
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem

# avtobus bi z indeksom i
# čas t  TO IŠČEMO
# B = produkt vseh bi
# Bi = B // bi

# Sistem kongruenc:
# t = bi - i (mod bi)   za vsak i

# Izrek pravi:
# t = vsota po i    (bi - i) * inv(Bi) * Bi
# kjer velja: (inv(Bi) * Bi) (mod bi) = 1

def inv(Bi, bi): # (inv * Bi) (mod bi) = 1
  for x in range(1, bi): # eden izmed teh bo inverz
    if (x * Bi) % bi == 1:
      return x

def part2():
  buses = [bus for bus in content[1].split(',')]
  vsota = 0
  B = 1 # delam celoten zmnožek vseh bi
  for bi in buses:
    if bi != 'x':
      B *= int(bi)

  for i, bi in enumerate(buses):
    if bi == 'x':
      continue
    bi = int(bi)
    Bi = B // bi
    vsota += ((bi - i) * inv(Bi, bi) * Bi) # po izreku

  return vsota % B # na vsakih B se ponavlja, zanima pa nas najmanjši tak čas


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