day = '6'

with open(f'2015/data/day_{day}.in', 'r', encoding='utf-8') as f:
    content = f.read().strip().split('\n')

##### Prva naloga #####
grid = [[0 for _ in range(1000)] for _ in range(1000)]
# grid[row][col]
if False: # calculate the first puzzle
    for e in content:
        if e[:7] == 'turn on':
            start_col = int(e[8:e.index(',')])
            rest1 = e[e.index(',') + 1:]
            start_row = int(rest1[:rest1.index(' ')])
            rest2 = rest1[rest1.index('t') + 8:]
            end_col = int(rest2[:rest2.index(',')])
            end_row = int(rest2[rest2.index(',') + 1:])
            for row in range(1000):
                for col in range(1000):
                    if start_row <= row <= end_row and start_col <= col <= end_col:
                        grid[row][col] = 1

        elif e[:8] == 'turn off':
            start_col = int(e[9:e.index(',')])
            rest1 = e[e.index(',') + 1:]
            start_row = int(rest1[:rest1.index(' ')])
            rest2 = rest1[rest1.index('t') + 8:]
            end_col = int(rest2[:rest2.index(',')])
            end_row = int(rest2[rest2.index(',') + 1:])
            for row in range(1000):
                for col in range(1000):
                    if start_row <= row <= end_row and start_col <= col <= end_col:
                        grid[row][col] = 0

        elif e[:6] == 'toggle':
            start_col = int(e[7:e.index(',')])
            rest1 = e[e.index(',') + 1:]
            start_row = int(rest1[:rest1.index(' ')])
            rest2 = rest1[rest1.index('t') + 8:]
            end_col = int(rest2[:rest2.index(',')])
            end_row = int(rest2[rest2.index(',') + 1:])
            for row in range(1000):
                for col in range(1000):
                    if start_row <= row <= end_row and start_col <= col <= end_col:
                        if grid[row][col] == 0:
                            grid[row][col] = 1
                        else:
                            grid[row][col] = 0

    on = 0
    for row in grid:
        for x in row:
            if x == 1:
                on += 1

##### Druga naloga #####
grid2 = [[0 for _ in range(1000)] for _ in range(1000)]
# grid2[row][col]
if False: # calculate the second puzzle
    for e in content:
        if e[:7] == 'turn on':
            start_col = int(e[8:e.index(',')])
            rest1 = e[e.index(',') + 1:]
            start_row = int(rest1[:rest1.index(' ')])
            rest2 = rest1[rest1.index('t') + 8:]
            end_col = int(rest2[:rest2.index(',')])
            end_row = int(rest2[rest2.index(',') + 1:])
            for row in range(1000):
                for col in range(1000):
                    if start_row <= row <= end_row and start_col <= col <= end_col:
                        grid2[row][col] += 1

        elif e[:8] == 'turn off':
            start_col = int(e[9:e.index(',')])
            rest1 = e[e.index(',') + 1:]
            start_row = int(rest1[:rest1.index(' ')])
            rest2 = rest1[rest1.index('t') + 8:]
            end_col = int(rest2[:rest2.index(',')])
            end_row = int(rest2[rest2.index(',') + 1:])
            for row in range(1000):
                for col in range(1000):
                    if start_row <= row <= end_row and start_col <= col <= end_col:
                        if grid2[row][col]:
                            grid2[row][col] -= 1


        elif e[:6] == 'toggle':
            start_col = int(e[7:e.index(',')])
            rest1 = e[e.index(',') + 1:]
            start_row = int(rest1[:rest1.index(' ')])
            rest2 = rest1[rest1.index('t') + 8:]
            end_col = int(rest2[:rest2.index(',')])
            end_row = int(rest2[rest2.index(',') + 1:])
            for row in range(1000):
                for col in range(1000):
                    if start_row <= row <= end_row and start_col <= col <= end_col:
                        grid2[row][col] = grid2[row][col] + 2

    on2 = 0
    for row in grid2:
        for x in row:
            on2 += x

def main():
  if 'on' in globals() and 'on2' in globals:
    s1 = on
    print(f'day {day}, puzzle 1: {s1}')
    s2 = on2
    print(f'day {day}, puzzle 2: {s2}')

    with open(f'2015/out/day_{day}_1.out', 'w', encoding='utf-8') as f:
      f.write(str(s1))
    with open(f'2015/out/day_{day}_2.out', 'w', encoding='utf-8') as f:
      f.write(str(s2))
  else:
      print('set bool values to true (lines 9, 59)')

main()

# day 6, puzzle 1: 377891
# day 6, puzzle 2: 14110788