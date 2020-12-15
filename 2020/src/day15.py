day = '15'

with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
  content = f.read() # '17,1,3,16,19,0'


##############################
##########  PART 1  ##########
##############################

# POMOŽNA ZA PRVOTNO REŠITEV PART1
# def razmik_od_zadnje_pojavitve1(sez, stevilo):
#   for i, kandidat in enumerate(sez[::-1][1:]):
#     if kandidat == stevilo:
#       return i + 1
#   return 0

def part1(n=2020):
  return part2(n)
  # SPODAJ: POLOVIČNO OPTIMIZIRANA REŠITEV (ŽE SEMI HITRA - MNOŽICA)
  # turns = [int(n) for n in content.split(',')]
  # bazen = set(turns[:-1])

  # zadnje_stevilo = turns[-1]
  # for _ in range(n - len(turns)):

  #   if zadnje_stevilo in bazen:
  #     novo_stevilo = razmik_od_zadnje_pojavitve1(turns, zadnje_stevilo)
  #     turns.append(novo_stevilo)
  #     zadnje_stevilo = novo_stevilo

  #   else: # novo zadnje_stevilo
  #     bazen.add(zadnje_stevilo)
  #     turns.append(0)
  #     zadnje_stevilo = 0
    
  # return turns[-1]


##############################
##########  PART 2  ##########
##############################

def part2(n=30000000): # cca 30s execution
  data = [int(n) for n in content.split(',')]
  turns = data[:-1]
  bazen = {st : i for i, st in enumerate(turns)}
  zadnje_stevilo = data[-1]
  
  while True:
    leng = len(turns)
    if leng + 1 == n:
      return zadnje_stevilo

    if zadnje_stevilo in bazen:
      turns.append(zadnje_stevilo)
      z = zadnje_stevilo # začasno shranim 'prejšnje zadnje_stevilo'
      zadnje_stevilo = leng - bazen[zadnje_stevilo]
      bazen[z] = leng

    else:
      turns.append(zadnje_stevilo)
      bazen[zadnje_stevilo] = leng
      zadnje_stevilo = 0


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