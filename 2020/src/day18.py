day = '18'

with open(f'2020/data/day_{day}.in', 'r', encoding='utf-8') as f:
  content = f.read().strip().split('\n')


##############################
##########  PART 1  ##########
##############################

def find_nth(haystack, needle, n): # index of nth occurence
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def no_brackets_left_to_right(expr): # brez oklepajev
    if expr.count('+') + expr.count('*') == 1:
      return eval(expr)
    else:
      i = find_nth(expr, ' ', 3)
      new_expr = str(eval(expr[:i])) + expr[i:] # zeroth operator evaluated
      return no_brackets_left_to_right(new_expr)

def evaluate1(expr): # with brackets
  if not ('(' in expr or ')' in expr):
    return no_brackets_left_to_right(expr)
  else: # we have brackets
    for i, x in enumerate(expr):
      if x == '(':
        bracket_index = i
      elif x == ')':
        one_bracket_expr = expr[bracket_index : i+1]
        partial_part = str(no_brackets_left_to_right(one_bracket_expr[1:-1]))
        closer_to_solution = expr.replace(one_bracket_expr, partial_part)
        return evaluate1(closer_to_solution)

def part1():
  return sum(evaluate1(row) for row in content)


##############################
##########  PART 2  ##########
##############################

def first_operator_plus(expr, plus_index): # returns bool
  return plus_index == (expr.index(' ') + 1)

def last_operator_plus(expr, plus_index): # returns bool
  spaces = [i for i, x in enumerate(expr) if x == ' ']
  return plus_index == (spaces[-1] - 1)

def get_last_expr(expr):
  spaces = [i for i, x in enumerate(expr) if x == ' ']
  if len(spaces) == 2:
    return expr
  else:
    i = spaces[-3]
    return expr[i+1 : ]

def get_middle_expr(expr, plus_index):
  spaces = [i for i, x in enumerate(expr) if x == ' ']
  for s in spaces:
    if s < plus_index:
      space_before_plus = s
  for s in spaces:
    if s > plus_index:
      space_after_plus = s
      break
  last_space = spaces[spaces.index(space_before_plus) - 1]
  next_space = spaces[spaces.index(space_after_plus) + 1]
  return expr[last_space+1 : next_space]

def no_brackets_pluses_first(expr): # brez oklepajev
    if not ('*' in expr and '+' in expr):
      return eval(expr)
    else: # we have (*) and (+)
      plus_index = expr.index('+')
      if first_operator_plus(expr, plus_index):
        e = expr[ : find_nth(expr, ' ', 3)]
        new_expr = expr.replace(e, str(eval(e)))
        return no_brackets_pluses_first(new_expr)
      elif last_operator_plus(expr, plus_index):
        e = get_last_expr(expr)
        new_expr = expr.replace(e, str(eval(e)))
        return no_brackets_pluses_first(new_expr)
      else: # plus in the middle
        e = get_middle_expr(expr, plus_index)
        new_expr = expr.replace(e, str(eval(e)))
        return no_brackets_pluses_first(new_expr)

def evaluate2(expr): # with brackets
  if not ('(' in expr or ')' in expr):
    return no_brackets_pluses_first(expr)
  else: # we have brackets
    for i, x in enumerate(expr):
      if x == '(':
        bracket_index = i
      elif x == ')':
        one_bracket_expr = expr[bracket_index : i+1]
        partial_part = str(no_brackets_pluses_first(one_bracket_expr[1:-1]))
        closer_to_solution = expr.replace(one_bracket_expr, partial_part)
        return evaluate2(closer_to_solution)

def part2():
  return sum(evaluate2(row) for row in content)


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

# Day 18, part 1: 9535936849815 in 42ms
# Day 18, part 2: 472171581333710 in 41ms