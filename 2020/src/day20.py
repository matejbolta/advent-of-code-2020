day = '20'

##############################
##########  PARSING  #########
##############################

def parse_input(day=day):
  with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
    raw_tiles = f.read().strip().split('\n\n')
  tiles = []
  for t in raw_tiles:
    rows = t.split('\n')
    id = int(rows[0][rows[0].index(' ')+1 : rows[0].index(':')])
    tiles.append((id, rows[1:]))
  return tiles


##############################
##########  PART 1  ##########
##############################

def show(t): # prikaz v konzoli
  for r in t:
    for z in r:
      print(z + ' ', end='')
    print()

def border_is_matching_specific(border, tile): # -> bool
  b1 = tile[1][0]
  b2 = tile[1][-1]
  b3, b4 = '', ''
  for row in tile[1]:
    b3 += row[0]
    b4 += row[-1]
  return any([b1==border,b2==border,b3==border,b4==border,b1[::-1]==border,b2[::-1]==border,b3[::-1]==border,b4[::-1]==border])

def border_is_matching_any(border, tile, tiles): # -> bool
  for t in tiles:
    if t != tile and border_is_matching_specific(border, t):
      return True
  return False

def count_matching_borders(tile, tiles):
  b1 = tile[1][0]
  b2 = tile[1][-1]
  b3, b4 = '', ''
  for row in tile[1]:
    b3 += row[0]
    b4 += row[-1]
  return sum(1 for b in [b1,b2,b3,b4] if border_is_matching_any(b, tile, tiles))
  
def part1():
  tiles = parse_input()
  corner_tiles = [t for t in tiles if count_matching_borders(t, tiles) == 2]
  rtr = 1
  for ct in corner_tiles:
    rtr *= ct[0]
  return rtr


##############################
##########  PART 2  ##########
##############################

'''
#  .  .  .  .  .  #  #  .  #
#  #  #  .  .  #  .  .  .  .
.  .  .  #  .  .  .  .  .  #
#  #  .  .  .  #  .  .  .  #
#  #  .  .  .  #  .  .  .  #
.  #  .  .  .  .  .  .  .  .
.  .  .  .  .  #  .  .  .  #
#  .  #  .  .  #  .  .  .  .
#  .  .  #  .  .  .  .  .  #
#  #  #  #  .  #  #  .  .  .
'''

##############################
########  ORIENTING  #########
##############################

def get_b(i, tile): # -> border 0,1,2,3
  if i == 0:
    return tile[0]
  elif i == 2:
    return tile[2]
  elif i == 1:
    return ''.join([row[0] for row in tile])
  elif i == 3:
    return ''.join([row[-1] for row in tile])
  else:
    assert False

def rotate(tile):
  id, t = tile
  t = [e for e in t]
  n0,n1,n2,n3,n4,n5,n6,n7,n8,n9 = '','','','','','','','','',''
  for row in t:
    n0 += row[9]
    n1 += row[8]
    n2 += row[7]
    n3 += row[6]
    n4 += row[5]
    n5 += row[4]
    n6 += row[3]
    n7 += row[2]
    n8 += row[1]
    n9 += row[0]
  return (id, [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])

def mirror(tile): # up down
  id, t = tile
  kopija = [e for e in t]
  t = kopija[::-1]
  return (id, t)

def border_matches(b, tile): # -> bool
  b0, b1, b2, b3 = get_b(0, tile[1]), get_b(1, tile[1]), get_b(2, tile[1]), get_b(3, tile[1])
  return b in [b0,b1,b2,b3,b0[::-1],b1[::-1],b2[::-1],b3[::-1]]

def how_to_rotate(sample, tile): # -> None / something
  b0, b1, b2, b3 = get_b(0, tile[1]), get_b(1, tile[1]), get_b(2, tile[1]), get_b(3, tile[1])
  a0, a1, a2, a3 = get_b(0, sample[1]), get_b(1, sample[1]), get_b(2, sample[1]), get_b(3, sample[1])
  b4, b5, b6, b7 = b0[::-1], b1[::-1], b2[::-1], b3[::-1]
  if border_matches(a0, tile):
    if a0 == b0:
      return 'm'
    if a0 == b1:
      return 'r'
    if a0 == b2:
      return ''
    if a0 == b3:
      return 'mrrr'
    if a0 == b4:
      return 'rr'
    if a0 == b5:
      return 'mr'
    if a0 == b6:
      return 'mrr'
    if a0 == b7:
      return 'rrr'
    assert False
  elif border_matches(a1, tile):
    if a1 == b0:
      return 'rrr'
    if a1 == b1:
      return 'mrr'
    if a1 == b2:
      return 'mrrr'
    if a1 == b3:
      return ''
    if a1 == b4:
      return 'mr'
    if a1 == b5:
      return 'rr'
    if a1 == b6:
      return 'r'
    if a1 == b7:
      return 'm'
    assert False
  elif border_matches(a2, tile):
    if a2 == b0:
      return ''
    if a2 == b1:
      return 'mrrr'
    if a2 == b2:
      return 'mrr'
    if a2 == b3:
      return 'r'
    if a2 == b4:
      return 'm'
    if a2 == b5:
      return 'rrr'
    if a2 == b6:
      return 'rr'
    if a2 == b7:
      return 'mr'
    assert False
  elif border_matches(a3, tile):
    if a3 == b0:
      return 'mrrr'
    if a3 == b1:
      return ''
    if a3 == b2:
      return 'rrr'
    if a3 == b3:
      return 'mrr'
    if a3 == b4:
      return 'r'
    if a3 == b5:
      return 'm'
    if a3 == b6:
      return 'mr'
    if a3 == b7:
      return 'rr'
    assert False
  else:
    return None

def orient_all_tiles(): # -> oriented tiles
  not_rotated_tiles = parse_input()
  rotated_tiles = [not_rotated_tiles[0]]
  previous_new_rot = [not_rotated_tiles[0]]
  not_rotated_tiles.remove(not_rotated_tiles[0])

  while not_rotated_tiles: # len(rotated_tiles) < 144:
    new_rot = []
    for t in previous_new_rot:
      new_og = []
      for t1 in not_rotated_tiles:
        how = how_to_rotate(t, t1)
        if how != None:
          new_og.append(t1)
          t2 = (t1[0], [e for e in t1[1]]) # t1
          for action in how:
            if action == 'r':
              t2 = rotate(t2)
            elif action == 'm':
              t2 = mirror(t2)
          new_rot.append(t2)
      for t in new_og:
        not_rotated_tiles.remove(t)
    rotated_tiles.extend(new_rot)
    previous_new_rot = [e for e in new_rot]

  return rotated_tiles

##############################
#########  LOCATING  #########
##############################

tiles = orient_all_tiles()
# t = tiles[0]

def where_do_tiles_match(sample, tile): # -> None / match_place
  b0, b1, b2, b3 = get_b(0, tile), get_b(1, tile), get_b(2, tile), get_b(3, tile)
  a0, a1, a2, a3 = get_b(0, sample), get_b(1, sample), get_b(2, sample), get_b(3, sample)
  if a0 == b2:
    return 'up'
  elif a2 == b0:
    return 'down'
  elif a3 == b1:
    return 'right'
  elif a1 == b3:
    return 'left'
  else:
    return None

if 0:
  NUM = 0
  located_tiles = [] # (id, loc, tile)
  located_tiles.append((tiles[NUM][0], (0, 0), tiles[NUM][1]))
  del tiles[NUM]

  while tiles: # len(located_tiles) < 144:
    newly_located = [] # id, loc, tile
    for id, (x, y), t in located_tiles:
      newly_located_og = []
      for (id1, t1) in tiles:
        match = where_do_tiles_match(t, t1)
        if match != None: # 'str' glede na t
          newly_located_og.append((id1, t1))
          if match == 'up':
            t2 = ((id1, (x, y+1), t1))
          elif match == 'down':
            t2 = ((id1, (x, y-1), t1))
          elif match == 'left':
            t2 = ((id1, (x-1, y), t1))
          elif match == 'right':
            t2 = ((id1, (x+1, y), t1))
          else:
            assert False
          newly_located.append(t2)
      for t in newly_located_og:
        tiles.remove(t)
    located_tiles.extend(newly_located)
    print(len(located_tiles))

# očitno nekaj ne dela ok pri rotacijah/zrcaljenjih
# ampak vse zgleda ok. preverjeno 1000krat


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

# Day 20, part 1: 12519494280967 in 131ms