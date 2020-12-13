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

# Tole je baza za vse nadaljevanje:
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem

# Imamo sistem enačb:
# t ≡ -o = k-o  (mod k)
#   ==> t % k = -o = k-o

# Kitajski izrek o ostankih pravi:
# t = sum(i) ((k-o) * inverz(Ki) * Ki)
# kjer je K produkt vseh k; Ki produkt vseh k, razen ki,
# inverz gledamo po modulu ki

# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modul_inverz(a, n): # Vrne inverz od a po modulu n
  # vrne x, kjer a * x = 1 (mod n)
  a = a % n
  if n == 1:
    return 1
  for x in range(1, n): 
    if ((a * x) % n == 1): # ko pridemo do inverza, ga vrnemo
      return x 

def part2():
  buses_raw = content[1].split(',')

  buses = []
  K = 1 # produkt
  for o, bus in enumerate(buses_raw):
    if bus != 'x':
      k = int(bus)
      o = o % k # da je o med 0 in k
      buses.append((o, k))
      K *= k # nakoncu dobimo celoten produkt v K
  
  vsota = 0
  for oi, ki in buses:
    Ki = K // ki # sledimo izreku
    inverz_Ki = modul_inverz(Ki, ki) # sledimo izreku

    # člen pride iz izreka
    clen_vsote = (ki-oi) * inverz_Ki * Ki # k - o = dejansko t % k, oz -o po modulu k
    vsota += clen_vsote
  
  return vsota % K # (vsaj) na vsakih K se ta dogodek ponovno zgodi


##############################
############ MAIN ############
##############################

import time

def main(redo_first=False, redo_second=True):
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