day = '11'

with open(f'2020/data/day_{day}.in') as f:
  content = f.read().strip().split('\n')

# testni content:
# content = ["L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"]

def prestej_vse_zasedene(table):
  counter = 0
  for i in range(len(table)):
    for j in range(len(table[0])):
      if table[i][j] == "#":
        counter += 1
  return counter


##############################
##########  PART 1  ##########
##############################

tabela = [[znak for znak in row] for row in content]

def prestej_zasedene1(m, n, table):
  counter = 0
  rows = len(table)
  cols = len(table[0])
  for i in range(max(0, (m-1)), min((rows), (m+2))):
    for j in range(max(0, (n-1)), min((cols), (n+2))):
      if (i, j) != (m, n) and table[i][j] == "#":
        counter += 1
  return counter

def make_step1():
  stara_tabela = [[znak for znak in row] for row in tabela] # skopira novo tabelo
  for i in range(len(tabela)):
    for j in range(len(tabela[0])):
      if stara_tabela[i][j] == "L" and prestej_zasedene1(i, j, stara_tabela) == 0:
        tabela[i][j] = "#"
      elif stara_tabela[i][j] == "#" and prestej_zasedene1(i, j, stara_tabela) >= 4:
        tabela[i][j] = "L"
  return # None

def part1():
  while True:
    stara_tabela = [[znak for znak in row] for row in tabela]
    make_step1()
    if stara_tabela == tabela:
      return prestej_vse_zasedene(tabela)


##############################
##########  PART 2  ##########
##############################

tabela2 = [[znak for znak in row] for row in content]

def prestej_zasedene2(m, n, table):
  counter = 0
  rows, cols = len(table), len(table[0])
  # desno gor
  if not (m == 0 or n == (cols-1)): # nismo na robu
    i, j = 1, 1
    while True:
      if table[m-i][n+j] == "#":
        counter += 1
        break
      elif table[m-i][n+j] == "L":
        break
      
      if (m-i) == 0 or (n+j) == (cols-1): # smo na robu
        break
      else: i, j = i+1, j+1
  
  # desno dol
  if not (m == (rows-1) or n == (cols-1)): # nismo na robu
    i, j = 1, 1
    while True:
      if table[m+i][n+j] == "#":
        counter += 1
        break
      elif table[m+i][n+j] == "L":
        break
      
      if (m+i) == (rows-1) or (n+j) == (cols-1): # smo na robu
        break
      else: i, j = i+1, j+1
  
  # levo gor
  if not (m == 0 or n == 0): # nismo na robu
    i, j = 1, 1
    while True:
      if table[m-i][n-j] == "#":
        counter += 1
        break
      elif table[m-i][n-j] == "L":
        break
      
      if (m-i) == 0 or (n-j) == 0: # smo na robu
        break
      else: i, j = i+1, j+1

  # levo dol
  if not (m == (rows-1) or n == 0): # nismo na robu
    i, j = 1, 1
    while True:
      if table[m+i][n-j] == "#":
        counter += 1
        break
      elif table[m+i][n-j] == "L":
        break
      
      if (m+i) == (rows-1) or (n-j) == 0: # smo na robu
        break
      else: i, j = i+1, j+1
  
  # dol
  if not (m == rows-1): # nismo na robu
    i = 1
    while True:
      if table[m+i][n] == "#":
        counter += 1
        break
      elif table[m+i][n] == "L":
        break
      
      if (m+i) == (rows-1): # smo na robu
        break
      else: i += 1
    
  # gor
  if not (m == 0): # nismo na robu
    i = 1
    while True:
      if table[m-i][n] == "#":
        counter += 1
        break
      elif table[m-i][n] == "L":
        break
      
      if (m-i) == 0: # smo na robu
        break
      else: i += 1
  
  # desno
  if not (n == cols-1): # nismo na robu
    j = 1
    while True:
      if table[m][n+j] == "#":
        counter += 1
        break
      elif table[m][n+j] == "L":
        break
      
      if (n+j) == (cols-1): # smo na robu
        break
      else: j += 1
  
  # levo
  if not (n == 0): # nismo na robu
    j = 1
    while True:
      if table[m][n-j] == "#":
        counter += 1
        break
      elif table[m][n-j] == "L":
        break
      
      if (n-j) == 0: # smo na robu
        break
      else: j += 1

  return counter

def make_step2():
  stara_tabela = [[znak for znak in row] for row in tabela2] # skopira novo tabelo
  for i in range(len(tabela2)):
    for j in range(len(tabela2[0])):
      if stara_tabela[i][j] == "L" and prestej_zasedene2(i, j, stara_tabela) == 0:
        tabela2[i][j] = "#"
      elif stara_tabela[i][j] == "#" and prestej_zasedene2(i, j, stara_tabela) >= 5:
        tabela2[i][j] = "L"
  return # None

def part2():
  while True:
    stara_tabela = [[znak for znak in row] for row in tabela2]
    make_step2()
    if stara_tabela == tabela2:
      return prestej_vse_zasedene(tabela2)


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