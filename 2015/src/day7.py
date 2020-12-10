with open(f'2015/data/day_7.in', 'r', encoding='utf-8') as f:
    content = f.read().strip().split('\n')

def binary(x): # 16-bit system
    x = int(x)
    return (16 - len(format(x, 'b'))) * '0' + format(x, 'b')

def decimal(x):
    return int(str(x), 2)

def and1(x, y): # x & y
    x, y = int(x), int(y)
    # return x & y
    x, y = binary(x), binary(y)
    s = ''
    for i in range(16):
        if int(x[i]) and int(y[i]):
            s += '1'
        else:
            s += '0'
    return decimal(s)

def or1(x, y): # x | y
    x, y = int(x), int(y)
    # return x | y
    x, y = binary(x), binary(y)
    s = ''
    for i in range(16):
        if int(x[i]) or int(y[i]):
            s += '1'
        else:
            s += '0'
    return decimal(s)

def not1(x): # ~ x
    x = int(x)
    # return (2 ** 16) + (~ x)
    x = binary(x)
    s = ''
    for c in x:
        if int(c):
            s += '0'
        else:
            s += '1'
    return decimal(s)

def lshift(x, n): # x << n
    x, n = int(x), int(n)
    # return x << n
    x = binary(x)
    while n > 0:
        x = x[1:] + x[0]
        n -= 1
    return decimal(x)

def rshift(x, n): # x >> n
    x, n = int(x), int(n)
    return x >> n
    # Z uporabo tegale nekaj ne dela pri velikih rotacijah (za 15)
    # Mislim, da je to napaka v zasnovi puzzla, ker imamo vse shranjeno v 16-bitni obliki.
    # in << tega ne upošteva.
    x = binary(x)
    while n > 0:
        x = x[-1] + x[:-1]
        n -= 1
    return decimal(x)


##### Prva naloga #####
ukazi = []
globalke = {} # Slovar z vsemi žicami/spremenljivkami + številkami do 2**16
for i in range(2**16 + 1):
    globalke[str(i)] = str(i)

if 1: # skonstruiraj ukaze kot tuple
    for row in content:
        if 'AND' in row:
            # print(row)
            ukazi.append((
                'AND',
                row[ : row.index(' ')],
                row[row.index('D')+2 : row.index('-')-1],
                row[row.index('>')+2 : ]
            ))
        elif 'OR' in row:
            ukazi.append((
                'OR',
                row[ : row.index(' ')],
                row[row.index('R')+2 : row.index('-')-1],
                row[row.index('>')+2 : ]
            ))
        elif 'NOT' in row:
            ukazi.append((
                'NOT',
                row[row.index('T')+2 : row.index('-')-1],
                row[row.index('>')+2 : ]
            ))
        elif 'RSHIFT' in row:
            ukazi.append((
                'RSHIFT',
                row[ : row.index(' ')],
                row[row.index('T')+2 : row.index('-')-1],
                row[row.index('>')+2 : ]
            ))
        elif 'LSHIFT' in row:
            ukazi.append((
                'LSHIFT',
                row[ : row.index(' ')],
                row[row.index('T')+2 : row.index('-')-1],
                row[row.index('>')+2 : ]
            ))
        else:
            ukazi.append((
                'ASSIGN',
                row[ : row.index(' ')],
                row[row.index('>')+2 : ]
            ))

vrhovni_ukazi = [ukaz for ukaz in ukazi]

def izvedljiv_ukaz(ukaz):
    if ukaz[0] == 'AND': # ('AND', 'eg', 'ei', 'ej')
        if all([ukaz[1] in globalke, ukaz[2] in globalke]):
            return True
    elif ukaz[0] == 'OR': # ('OR', 'eg', 'ei', 'ej')
        if all([ukaz[1] in globalke, ukaz[2] in globalke]):
            return True
    elif ukaz[0] == 'NOT': # ('NOT', 'lo', 'lp')
        if ukaz[1] in globalke:
            return True
    elif ukaz[0] == 'RSHIFT': # ('RSHIFT', 'b', '2', 'd')
        if all([ukaz[1] in globalke, ukaz[2] in globalke]):
            return True
    elif ukaz[0] == 'LSHIFT': # ('LSHIFT', 'kh', '1', 'lb')
        if all([ukaz[1] in globalke, ukaz[2] in globalke]):
            return True
    elif ukaz[0] == 'ASSIGN': # ('ASSIGN', '44430', 'b'),
        if ukaz[1] in globalke:
            return True
    # print(f'ta ukaz {ukaz[0]} ni izvedljiv ker sm prišel do konca')
    return False

def izvedi_ukaz(ukaz):
    if ukaz[0] == 'AND': # ('AND', 'd', 'j', 'l')
        globalke[ukaz[3]] = and1(globalke[ukaz[1]], globalke[ukaz[2]])
        return True
    elif ukaz[0] == 'OR': # ('OR', 'kk', 'kv', 'kw')
        globalke[ukaz[3]] = or1(globalke[ukaz[1]], globalke[ukaz[2]])
        return True
    elif ukaz[0] == 'NOT': # ('NOT', 'go', 'gp')
        globalke[ukaz[2]] = not1(globalke[ukaz[1]])
        return True
    elif ukaz[0] == 'RSHIFT': # ('RSHIFT', 'lf', '5', 'li')
        globalke[ukaz[3]] = rshift(globalke[ukaz[1]], globalke[ukaz[2]])
        return True
    elif ukaz[0] == 'LSHIFT': # ('LSHIFT', 'c', '1', 't')
        globalke[ukaz[3]] = lshift(globalke[ukaz[1]], globalke[ukaz[2]])
        return True
    elif ukaz[0] == 'ASSIGN': # ('ASSIGN', '44430', 'b')
        globalke[ukaz[2]] = globalke[ukaz[1]]
        return True
    print('ukaza nisem izvedel ker sem prišel do konca')
    return False

if 1: # izvedi ukaze
    while ukazi:
        stari_ukazi = [ukaz for ukaz in ukazi]
        ukazi = []
        for ukaz in stari_ukazi:
            if izvedljiv_ukaz(ukaz):
                izvedi_ukaz(ukaz)
            else:
                ukazi.append(ukaz)


##### Druga naloga #####
ukazi2 = [ukaz for ukaz in vrhovni_ukazi]
globalke2 = {} # Slovar z vsemi žicami/spremenljivkami + številkami do 2**16
for i in range(2**16 + 1):
    globalke2[str(i)] = str(i)

def izvedljiv_ukaz2(ukaz):
    if ukaz[0] == 'AND': # ('AND', 'eg', 'ei', 'ej')
        if all([ukaz[1] in globalke2, ukaz[2] in globalke2]):
            return True
    elif ukaz[0] == 'OR': # ('OR', 'eg', 'ei', 'ej')
        if all([ukaz[1] in globalke2, ukaz[2] in globalke2]):
            return True
    elif ukaz[0] == 'NOT': # ('NOT', 'lo', 'lp')
        if ukaz[1] in globalke2:
            return True
    elif ukaz[0] == 'RSHIFT': # ('RSHIFT', 'b', '2', 'd')
        if all([ukaz[1] in globalke2, ukaz[2] in globalke2]):
            return True
    elif ukaz[0] == 'LSHIFT': # ('LSHIFT', 'kh', '1', 'lb')
        if all([ukaz[1] in globalke2, ukaz[2] in globalke2]):
            return True
    elif ukaz[0] == 'ASSIGN': # ('ASSIGN', '44430', 'b'),
        if ukaz[1] in globalke2:
            return True
    # print(f'ta ukaz {ukaz[0]} ni izvedljiv ker sm prišel do konca')
    return False

def izvedi_ukaz2(ukaz):
    if ukaz[0] == 'AND': # ('AND', 'd', 'j', 'l')
        globalke2[ukaz[3]] = and1(globalke2[ukaz[1]], globalke2[ukaz[2]])
        return True
    elif ukaz[0] == 'OR': # ('OR', 'kk', 'kv', 'kw')
        globalke2[ukaz[3]] = or1(globalke2[ukaz[1]], globalke2[ukaz[2]])
        return True
    elif ukaz[0] == 'NOT': # ('NOT', 'go', 'gp')
        globalke2[ukaz[2]] = not1(globalke2[ukaz[1]])
        return True
    elif ukaz[0] == 'RSHIFT': # ('RSHIFT', 'lf', '5', 'li')
        globalke2[ukaz[3]] = rshift(globalke2[ukaz[1]], globalke2[ukaz[2]])
        return True
    elif ukaz[0] == 'LSHIFT': # ('LSHIFT', 'c', '1', 't')
        globalke2[ukaz[3]] = lshift(globalke2[ukaz[1]], globalke2[ukaz[2]])
        return True
    elif ukaz[0] == 'ASSIGN': # ('ASSIGN', '44430', 'b')
        globalke2[ukaz[2]] = globalke2[ukaz[1]]
        return True
    print('ukaza nisem izvedel')
    return False

if 1: # izvedi ukaze
    while ukazi2:
        stari_ukazi2 = [ukaz for ukaz in ukazi2]
        ukazi2 = []
        for ukaz in stari_ukazi2:
            if izvedljiv_ukaz2(ukaz):
                izvedi_ukaz2(ukaz)
                globalke2['b'] = '3176'
            else:
                ukazi2.append(ukaz)


def main():
    if 'a' in globalke:
        s1 = globalke['a']
        print(f'day 7, puzzle 1: {s1}')
    if 'a' in globalke2:
        s2 = globalke2['a']
        print(f'day 7, puzzle 2: {s2}')

    with open(f'2015/out/day_7_1.out', 'w', encoding='utf-8') as f:
        f.write(str(s1))
    with open(f'2015/out/day_7_2.out', 'w', encoding='utf-8') as f:
        f.write(str(s2))

main()