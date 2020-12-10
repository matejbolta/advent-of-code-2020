day = '2'

with open(f'2015/data/day_{day}.in', 'r', encoding='utf-8') as f:
    content = f.read().strip().split('\n')

def make_tup(row):
    i = row.index('x')
    a = row[:i]
    row = row[i + 1:]
    i = row.index('x')
    b = row[:i]
    c = row[i + 1:]
    return int(a), int(b), int(c)

def area(a, b, c):
    return 2 * (a*b + a*c + b*c)

##### Prva naloga #####
paper1 = 0
for row in content:
    a, b, c = make_tup(row)
    paper1 += area(a, b, c)
    paper1 += min(a*b, b*c, a*c)

##### Druga naloga #####
ribbon2 = 0
for row in content:
    a, b, c = make_tup(row)
    ribbon2 += min(2*(a+b), 2*(a+c), 2*(b+c))
    ribbon2 += a*b*c


def main():
    s1 = str(paper1)
    print(f'day {day}, puzzle 1: {s1}')
    s2 = str(ribbon2)
    print(f'day {day}, puzzle 2: {s2}')

    with open(f'2015/out/day_{day}_1.out', 'w', encoding='utf-8') as f:
        f.write(s1)
    with open(f'2015/out/day_{day}_2.out', 'w', encoding='utf-8') as f:
        f.write(s2)

main()