day = '5'

with open(f'2015/data/day_{day}.in', 'r', encoding='utf-8') as f:
    content = f.read().strip().split('\n')

##### Prva naloga #####
nice1 = 0
for row in content:
    vowels = 0
    for c in 'aeiou':
        vowels += row.count(c)
    if vowels < 3:
        continue
    
    second_check = False
    for i in range(len(row) - 1):
        if row[i] == row[i+1]:
            second_check = True
            break
    if not second_check:
        continue
    
    third_check = True
    for s in ['ab', 'cd', 'pq', 'xy']:
        if s in row:
            third_check = False
            break
    if not third_check:
        continue
    
    nice1 += 1

##### Druga naloga #####
nice2 = 0
for row in content: #content:
    check_first = False
    for i in range(len(row) - 3):
        pair = row[i] + row[i + 1]
        row1 = row[i + 2:]
        if pair in row1:
            check_first = True
    if not check_first:
        continue

    check_second = False
    for i in range(len(row) - 2):
        if row[i] == row[i + 2]:
            check_second = True
    if not check_second:
        continue
    
    print(row)
    nice2 += 1

def main():
  s1 = nice1
  print(f'day {day}, puzzle 1: {s1}')
  s2 = nice2
  print(f'day {day}, puzzle 2: {s2}')

  with open(f'2015/out/day_{day}_1.out', 'w', encoding='utf-8') as f:
    f.write(str(s1))
  with open(f'2015/out/day_{day}_2.out', 'w', encoding='utf-8') as f:
    f.write(str(s2))

main()