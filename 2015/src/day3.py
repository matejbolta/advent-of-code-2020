day = '3'

with open(f'2015/data/day_{day}.in', 'r', encoding='utf-8') as f:
    content = f.read()


##### Prva naloga #####
houses1 = {(0, 0)}
x, y = 0, 0
for move in content:
    if move == '^':
        y = y + 1
    elif move == 'v':
        y = y - 1
    elif move == '>':
        x = x + 1
    elif move == '<':
        x = x - 1
    loc = (x, y)
    houses1.add(loc)

##### Druga naloga #####
houses2 = {(0, 0)}
x1, y1 = 0, 0
x2, y2 = 0, 0
for i, move in enumerate(content):
    if not i % 2: # santa
        if move == '^':
            y1 = y1 + 1
        elif move == 'v':
            y1 = y1 - 1
        elif move == '>':
            x1 = x1 + 1
        elif move == '<':
            x1 = x1 - 1
    loc1 = (x1, y1)
    houses2.add(loc1)

    if i % 2: # robo santa
        if move == '^':
            y2 = y2 + 1
        elif move == 'v':
            y2 = y2 - 1
        elif move == '>':
            x2 = x2 + 1
        elif move == '<':
            x2 = x2 - 1
    loc2 = (x2, y2)
    houses2.add(loc2)


def main():
  s1 = str(len(houses1))
  print(f'day {day}, puzzle 1: {s1}')
  s2 = str(len(houses2))
  print(f'day {day}, puzzle 2: {s2}')

  with open(f'2015/out/day_{day}_1.out', 'w', encoding='utf-8') as f:
    f.write(s1)
  with open(f'2015/out/day_{day}_2.out', 'w', encoding='utf-8') as f:
    f.write(s2)

main()