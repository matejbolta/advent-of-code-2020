import hashlib
day = '4'
with open(f'2015/data/day_{day}.in', 'r', encoding='utf-8') as f:
    input = f.read()

##### Prva naloga #####
##### Druga naloga #####
def gen(x):
    i = 1
    while True:
        md5 = hashlib.md5(f'{input}{i}'.encode('utf-8')).hexdigest()
        if md5[:x] == x * '0':
            return i
        i += 1

def main():
  s1 = str(gen(5))
  print(f'day {day}, puzzle 1: {s1}')
  s2 = str(gen(6))
  print(f'day {day}, puzzle 2: {s2}')

  with open(f'2015/out/day_{day}_1.out', 'w', encoding='utf-8') as f:
    f.write(s1)
  with open(f'2015/out/day_{day}_2.out', 'w', encoding='utf-8') as f:
    f.write(s2)

main()