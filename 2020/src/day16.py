day = '16'

##############################
##########  PARSING  #########
##############################

with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
  content = f.read().strip()

if 'parse_input': # <==> True
  first_part, tickets = content.split('\n\nnearby tickets:\n')
  polja, my_ticket = first_part.split('\n\nyour ticket:\n')
  my_ticket = [int(n) for n in my_ticket.split(',')]
  tickets = [[int(n) for n in row.split(',')] for row in tickets.split('\n')]
  polja = polja.split('\n')
  fields = []
  for polje in polja:
    word = polje[:polje.index(':')]
    ostalo = polje[polje.index(':')+2 :]
    a = int(ostalo[:ostalo.index('-')])
    b = int(ostalo[ostalo.index('-')+1:ostalo.index('o')-1])
    ostalo = ostalo[ostalo.index('r')+2:]
    c = int(ostalo[:ostalo.index('-')])
    d = int(ostalo[ostalo.index('-')+1:])
    fields.append((word, (a, b), (c, d)))


##############################
##########  PART 1  ##########
##############################

def make_mno():
  # parsing fields even further - building set mno
  mno = set()
  for field in fields: # ('departure location', (34, 269), (286, 964))
    for n in range(field[1][0], field[1][1]+1):
      mno.add(n)
    for n in range(field[2][0], field[2][1]+1):
      mno.add(n)
  return mno

def part1():
  mno = make_mno()
  suma = 0
  for t in tickets:
    for n in t:
      if not n in mno:
        suma += n
  return suma


##############################
##########  PART 2  ##########
##############################

def filter_tickets(ticks):
  mno = make_mno()
  valid = []
  for t in ticks:
    ok = True
    for n in t:
      if not n in mno:
        ok = False
        break
    if ok:
      valid.append(t)
  return valid

def ustrezna_polja(tickets, i, fields):
  stevila = []
  for ticket in tickets:
    stevila.append(ticket[i])
  valid_fields = []
  for field in fields:
    field_ok = True
    for st in stevila:
      if not st in field[1]:
        field_ok = False
        break
    if field_ok:
      valid_fields.append(field)
  return [polje[0] for polje in valid_fields]

def part2(ticks=tickets, old_fields=fields, my_ticket=my_ticket):
  tickets = filter_tickets(ticks)
  fields = []
  for (name, (a, b), (c, d)) in old_fields:
    mn = set()
    for n in range(a, b+1):
      mn.add(n)
    for n in range(c, d+1):
      mn.add(n)
    fields.append((name, mn))
  
  slovar_vozovnic = {} # indeks : vsa mozna polja (se podirajo kot domine)
  for i in range(len(tickets[0])):
    polja_i = ustrezna_polja(tickets, i, fields)
    slovar_vozovnic[i] = polja_i

  koncni_slovar = {} # indeks : pravilno polje
  zavzeta_polja = set()
  for st in range(1, len(tickets[0])+1):
    for indeks, polja in slovar_vozovnic.items():
      if len(polja) == st:
        obravnavani = (indeks, polja)
    indeks, polja = obravnavani
    for polje in polja:
      if not polje in zavzeta_polja:
        koncni_slovar[indeks] = polje
        zavzeta_polja.add(polje)
  
  produkt = 1
  for indeks, field in koncni_slovar.items():
    if ' ' in field and field[:field.index(' ')] == 'departure':
      produkt *= (my_ticket[indeks])
  
  return produkt


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