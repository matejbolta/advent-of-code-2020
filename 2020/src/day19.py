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

# DISCLAIMER: spodnja koda je groza, ne glej ker noces videt tega

def part2():
  # minimalno osem levo in sestnajst desno. (potem pa z večkratniki)
  # 8: 42 | 42 8
  # 11: 42 31 | 42 11 31

  initial_rules, final_rules, all_messages = parse_input()
  execute_all_rules(initial_rules, final_rules)

  # lens = {len(m) for m in all_messages}
  # # {24, 32, 40, 48, 56, 64, 72, 80}
  messages = [m for m in all_messages if not m in final_rules[0]] # 249
  def messages_of_len(n, messages=messages):
    return [m for m in messages if len(m) == n]
  mess24 = messages_of_len(24) #  9
  mess32 = messages_of_len(32) # 67
  mess40 = messages_of_len(40) # 71
  mess48 = messages_of_len(48) # 36
  mess56 = messages_of_len(56) # 32
  mess64 = messages_of_len(64) # 18
  mess72 = messages_of_len(72) #  7
  mess80 = messages_of_len(80) #  5
  mess88 = messages_of_len(88) #  1
  mess96 = messages_of_len(96) #  3

  a, b, c = final_rules[8], final_rules[42], final_rules[31]

  finally_gucci_good_messages = {m for m in all_messages if m in final_rules[0]} # will be updated
  # print(len(finally_gucci_good_messages)) # 149

  for m in mess24: # 24 = 8+16
    if (
      (m[0:8] in a) and (m[8:16] in b) and (m[16:24] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 149, +0 (od 9ih)

  for m in mess32: # 32 = 8+8+16
    if (
      (m[0:8] in a) and (m[8:16] in a) and (m[16:24] in b) and (m[24:32] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 202, +53 (od 67ih)

  for m in mess40: # 40 = 8+8+8+16 | 8+16+16
    if (
      (m[0:8]   in a) and (m[8:16] in a) and (m[16:24] in a) and (m[24:32] in b) and
      (m[32:40] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16] in b) and (m[16:24] in b) and (m[24:32] in c) and
      (m[32:40] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 264, +62 (od 71ih)

  for m in mess48: # 48 = 8+8+8+8+16 | 8+8+16+16
    if (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in b) and (m[40:48] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in b) and (m[24:32] in b) and
      (m[32:40] in c) and (m[40:48] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 294, +30 (od 36ih)

  for m in mess56: # 56 = 8+8+8+8+8+16 | 8+8+8+16+16 | 8+16+16+16
    if (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in b) and (m[48:56] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in b) and
      (m[32:40] in b) and (m[40:48] in c) and (m[48:56] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in b) and (m[16:24] in b) and (m[24:32] in b) and
      (m[32:40] in c) and (m[40:48] in c) and (m[48:56] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 316, +22 (od 32ih)

  for m in mess64: # 64 = 8+8+8+8+8+8+16 | 8+8+8+8+16+16 | 8+8+16+16+16
    if (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in b) and (m[56:64] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in b) and (m[40:48] in b) and (m[48:56] in c) and (m[56:64] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in b) and (m[24:32] in b) and
      (m[32:40] in b) and (m[40:48] in c) and (m[48:56] in c) and (m[56:64] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 328, +12 (od 18ih)

  for m in mess72: # 72 = 8+8+8+8+8+8+8+16 | 8+8+8+8+8+16+16 | 8+8+8+16+16+16 | 8+16+16+16+16
    if (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in a) and (m[56:64] in b) and
      (m[64:72] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in b) and (m[48:56] in b) and (m[56:64] in c) and
      (m[64:72] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in b) and
      (m[32:40] in b) and (m[40:48] in b) and (m[48:56] in c) and (m[56:64] in c) and
      (m[64:72] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in b) and (m[16:24] in b) and (m[24:32] in b) and
      (m[32:40] in b) and (m[40:48] in c) and (m[48:56] in c) and (m[56:64] in c) and
      (m[64:72] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 331, +3 (od 7ih)

  for m in mess80: # 80 = 8+8+8+8+8+8+8+8+16 | 8+8+8+8+8+8+16+16 | 8+8+8+8+16+16+16 | 8+8+16+16+16+16
    if (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in a) and (m[56:64] in a) and
      (m[64:72] in b) and (m[72:80] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in b) and (m[56:64] in b) and
      (m[64:72] in c) and (m[72:80] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in b) and (m[40:48] in b) and (m[48:56] in b) and (m[56:64] in c) and
      (m[64:72] in c) and (m[72:80] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in b) and (m[24:32] in b) and
      (m[32:40] in b) and (m[40:48] in b) and (m[48:56] in c) and (m[56:64] in c) and
      (m[64:72] in c) and (m[72:80] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 332, +1 (od 5ih)

  for m in mess88: # 88 = 8+8+8+8+8+8+8+8+8+16 | 8+8+8+8+8+8+8+16+16 | 8+8+8+8+8+16+16+16 | 8+8+8+16+16+16+16 | 8+16+16+16+16+16
    if (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in a) and (m[56:64] in a) and
      (m[64:72] in a) and (m[72:80] in b) and (m[80:88] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in a) and (m[56:64] in b) and
      (m[64:72] in b) and (m[72:80] in c) and (m[80:88] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in b) and (m[48:56] in b) and (m[56:64] in b) and
      (m[64:72] in c) and (m[72:80] in c) and (m[80:88] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in b) and
      (m[32:40] in b) and (m[40:48] in b) and (m[48:56] in b) and (m[56:64] in c) and
      (m[64:72] in c) and (m[72:80] in c) and (m[80:88] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in b) and (m[16:24] in b) and (m[24:32] in b) and
      (m[32:40] in b) and (m[40:48] in b) and (m[48:56] in c) and (m[56:64] in c) and
      (m[64:72] in c) and (m[72:80] in c) and (m[80:88] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 332, +0 (od enega)

  for m in mess96: # 96 = 8+8+8+8+8+8+8+8+8+8+16 | 8+8+8+8+8+8+8+8+16+16 | 8+8+8+8+8+8+16+16+16 | 8+8+8+8+16+16+16+16 | 8+8+16+16+16+16+16
    if (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in a) and (m[56:64] in a) and
      (m[64:72] in a) and (m[72:80] in a) and (m[80:88] in b) and (m[88:96] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in a) and (m[56:64] in a) and
      (m[64:72] in b) and (m[72:80] in b) and (m[80:88] in c) and (m[88:96] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in a) and (m[40:48] in a) and (m[48:56] in b) and (m[56:64] in b) and
      (m[64:72] in b) and (m[72:80] in c) and (m[80:88] in c) and (m[88:96] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in a) and (m[24:32] in a) and
      (m[32:40] in b) and (m[40:48] in b) and (m[48:56] in b) and (m[56:64] in b) and
      (m[64:72] in c) and (m[72:80] in c) and (m[80:88] in c) and (m[88:96] in c)
    ):
      finally_gucci_good_messages.add(m)
    elif (
      (m[0:8]   in a) and (m[8:16]  in a) and (m[16:24] in b) and (m[24:32] in b) and
      (m[32:40] in b) and (m[40:48] in b) and (m[48:56] in b) and (m[56:64] in c) and
      (m[64:72] in c) and (m[72:80] in c) and (m[80:88] in c) and (m[88:96] in c)
    ):
      finally_gucci_good_messages.add(m)
  # print(len(finally_gucci_good_messages)) # 332, +0 (od treh)

  return len(finally_gucci_good_messages)


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

# grozna rešitev druge naloge ampak ura je 3 zjutri in sem vesel :)
# part2 deluje samo na podanem inputu (kar je bilo namignjeno tudi v navodilih)

# Day 19, part 1: 149 in 852ms
# Day 19, part 2: 332 in 893ms