day = '19'

##############################
##########  PARSING  #########
##############################

def parse_input(day=day):
  with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
    rules, messages = f.read().strip().split('\n\n')
  initial_rules, final_rules = {}, {}
  for rule in rules.split('\n'):
    if '"' in rule:
      indeks = int(rule[ : rule.index(':')])
      value = rule[rule.index('"')+1 : -1]
      final_rules[indeks] = [value]
    else:
      indeks = int(rule[ : rule.index(':')])
      rest = rule[rule.index(':')+2 : ]
      initial_rules[indeks] = []
      if '|' in rule:
        rest = rest.split(' | ')
        for opt in rest:
          if ' ' in opt:
            fst = int(opt[ : opt.index(' ')])
            snd = int(opt[opt.index(' ')+1 : ])
            initial_rules[indeks].append([fst, snd])
          else:
            initial_rules[indeks].append([int(opt)])
      else:
        if ' ' in rest:
          fst = int(rest[ : rest.index(' ')])
          snd = int(rest[rest.index(' ')+1 : ])
          initial_rules[indeks] = [[fst, snd]]
        else:
            initial_rules[indeks].append([int(rest)])
  return initial_rules, final_rules, messages.split('\n')


##############################
##########  PART 1  ##########
##############################

def rule_is_executable(key, initial_rules, final_rules): # int -> bool
  value = initial_rules[key]
  needed_rules = []
  for sez in value:
    for num in sez:
      needed_rules.append(num)
  for needed_key in needed_rules:
    if not needed_key in final_rules:
      return False
  return True

def execute_rule(key, initial_rules, final_rules): # int -> None
  all_matches = set()
  value = initial_rules[key]
  for sez in value:
    if len(sez) == 1: # sez[0]
      for opt in final_rules[sez[0]]:
        all_matches.add(opt)
    elif len(sez) == 2: # sez[0] sez[1]
      options0 = final_rules[sez[0]]
      options1 = final_rules[sez[1]]
      for opt0 in options0:
        for opt1 in options1:
          opt = opt0 + opt1
          all_matches.add(opt)
  final_rules[key] = all_matches
  return ##

def execute_all_rules(initial_rules, final_rules):
  while initial_rules:
    executed_this_round = []
    for rule_key in initial_rules:
      if rule_is_executable(rule_key, initial_rules, final_rules):
        execute_rule(rule_key, initial_rules, final_rules)
        executed_this_round.append(rule_key)
    for key in executed_this_round:
      del initial_rules[key]
  return ##

def part1():
  initial_rules, final_rules, messages = parse_input()
  execute_all_rules(initial_rules, final_rules)
  return sum(1 for m in messages if m in final_rules[0])


##############################
##########  PART 2  ##########
##############################

# def max_length_dict(dic):
#   m = 0
#   for x in dic:
#     m = max(m, len(x))
#   return m

# 8: n*42                 # so dolžine 8n  # rabimo vse do len 80
# 11: m*(42 31)         # so dolžine 16m   # rabimo vse do len 88
# 0: n*42 m*(42 31)      # so dolžine najmanj 24    8-0-88, 80-0-16
#                                  # najdaljši messig: 96

# initial_rules, final_rules, messages = parse_input()
# execute_all_rules(initial_rules, final_rules)
# del final_rules[0] # 2097152
# del final_rules[8] # 128, tudi 42
# del final_rules[11] # 16384

# options_8 = final_rules[42]
# baza_8 = final_rules[42]
# for _ in range(2): # enkrat že mamo, še devetkrat
#   mozni = set()
#   leng = max_length_dict(options_8)
#   for obstojeci in options_8:
#     if len(obstojeci) == leng:
#       for bazni in baza_8:
#         mozni.add(obstojeci+bazni)
#   options_8.update(mozni)
# final_rules[8] = options_8

# 128                      8
# 16384                    16
# 2097152
# 268435456                32
# 34359738368
# 4398046511104            48
# 562949953421312
# 72057594037927936
# 9223372036854775808      72
# 1180591620717411303424   80

# to je 10**21, triljarda. toliko elementov hočemo spravit v options_8
# kar povzroči MemoryError. Nevem kako bi to naredil bolj učinkovito,
# saj rabimo poljubno kombinacijo elementov iz final_rules[42] dolžin do dolžine 80.

# kasneje, za 11ko, bi rabili manj korako, saj je posamezen dolžine 16,
# šli pa bi do dolžine 80 (5 krat)

def part2():
  pass


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

# Day 19, part 1: 149 in 986ms
# rip part 2