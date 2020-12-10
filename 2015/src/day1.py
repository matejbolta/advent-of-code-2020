day = '1'

with open(f'2015/data/day_{day}.in', 'r', encoding='utf-8') as f:
    content = f.read()

##### Prva naloga #####
floor1 = 0
for p in content:
    if p == '(':
        floor1 += 1
    else:
        floor1 -= 1

##### Druga naloga #####
floor2 = 0
for i, p in enumerate(content):
    if p == '(':
        floor2 += 1
    else:
        floor2 -= 1
    if floor2 == -1:
        s = i + 1
        break

def main():
  s1 = str(floor1)
  print(f'day {day}, puzzle 1: {s1}')
  s2 = str(s)
  print(f'day {day}, puzzle 2: {s2}')

  with open(f'2015/out/day_{day}_1.out', 'w', encoding='utf-8') as f:
      f.write(s1)
  with open(f'2015/out/day_{day}_2.out', 'w', encoding='utf-8') as f:
      f.write(s2)

main()