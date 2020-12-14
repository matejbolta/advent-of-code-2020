day = '14'

with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
  content = f.read().strip().split('\n')

data = []
for row in content:
  if row[:4] == 'mask':
    data.append(('mask', row[7:]))
  elif row[:3] == 'mem':
    data.append(('mem', row[row.index('[')+1 : row.index(']')], row[row.index('=')+2 : ]))


##############################
##########  PART 1  ##########
##############################

def binary(x): # 36-bit system
    return (36 - len(format(int(x), 'b'))) * '0' + format(int(x), 'b')

def decimal(x):
    return int(str(x), 2)

def apply_mask(mask, num):
  s = ''
  for m, n in zip(mask, binary(num)):
    if m == 'X':
      s += n
    elif m == '1':
      s += '1'
    elif m == '0':
      s += '0'
    else:
      assert False
  assert len(s) == 36
  return decimal(s)

def part1():
  slovar = {}
  for row in data:
    if row[0] == 'mask':
      mask = row[1]
    elif row[0] == 'mem':
      v = apply_mask(mask, row[2])
      slovar[row[1]] = v

  vsota = 0
  for v in slovar.values():
    vsota += v
  return vsota


##############################
##########  PART 2  ##########
##############################
from itertools import permutations

def apply_mask2(mask, num):
  s = ''
  for m, n in zip(mask, binary(num)):
    if m == 'X':
      s += 'X'
    elif m == '1':
      s += '1'
    elif m == '0':
      s += n
    else:
      assert False
  assert len(s) == 36
  return s

def vstavi_x(s, perm):
  assert len(perm) == s.count('X')
  p = [a for a in perm]
  koncni = ''
  indeks = 0
  for znak in s:
    if znak == 'X':
      koncni += p[indeks]
      indeks += 1
    else:
      koncni += znak

  return koncni

def all_possibles(s):
  l = []
  xsov = s.count('X')

  for st_enic in range(xsov+1):
    niz = (st_enic * '1') + ((xsov-st_enic) * '0')
    perms = [''.join(p) for p in permutations(niz)] # list

    for perm in perms:
      kljuc = vstavi_x(s, perm)
      l.append(decimal(kljuc))

  return l

def part2():
  slovar = {}
  # kje = 1
  for row in data:
    if row[0] == 'mask':
      mask = row[1]
    elif row[0] == 'mem':
      k = apply_mask2(mask, row[1])
      keys = all_possibles(k) # list of keys
      for k in keys:
        slovar[k] = row[2]
      # print(f'naredil mem št {kje}') # jih je 442
      # kje += 1
  # print(f'dolzina slovarja: {len(slovar)}')
  vsota = 0
  for v in slovar.values():
    vsota += int(v)
  return vsota


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