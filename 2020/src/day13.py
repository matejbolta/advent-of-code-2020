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

from math import gcd
from functools import reduce

def lcm(sez):
  return reduce(lambda a,b: a*b // gcd(a,b), sez)
# 581'610'429'053'251
# 100'000'000'000'000

# 19 -0
# 41 -9
# 37 -13
# 367 -19
# 13 -32
# 17 -36
# 29 -48
# 373 -50
# 23 -73

# content = [None, '67,7,x,59,61'] # 1'261'476
# content = [None, '1789,37,47,1889'] # 1'202'161'486



def part2():
  # buses = []
  # for t in content[1].split(','):
  #   if t == 'x':
  #     buses.append(0)
  #   else:
  #     buses.append(int(t))

  # maks = max(buses)
  # maks_i = buses.index(maks)

  buses = [(19, 0), (41, 9), (37, 13), (367, 19), (13, 32), (17, 36), (29, 48), (373, 50), (23, 73)]

  maks = 373
  maks_i = 50

  for t in itertools.count((maks-maks_i), maks):
    if not (t + maks_i) % ((10**9) * maks):
      print(t // (10**9), 'miljard')

    all_ok = True

    # for i, bus in enumerate(buses):
    #   if not bus:
    #     continue
    #   elif (t + i) % bus:
    #     all_ok = False
    #     break
    for bus, i in buses:
      if (t + i) % bus:
        all_ok = False
        break

    if all_ok:
      return t


##############################
############ MAIN ############
##############################

import time

def main(redo_first=True, redo_second=False):
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