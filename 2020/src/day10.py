# parsanje inputa
with open("data/day_10.in", 'r', encoding="utf-8") as file:
  content = file.read()
input = [0] + [int(x) for x in content.strip().split("\n")]
input = input + [max(input) + 3]
input.sort()
#############################################
# grajenje slovarja
slovar = {}
for i, x in enumerate(input):
  if i < len(input) - 3:
    slovar[x] = [input[i+1]]
    if input[i+3] - x <= 3:
      slovar[x].extend([input[i+2], input[i+3]])
    elif input[i+2] - x <= 3:
      slovar[x].extend([input[i+2]])
  elif i < len(input) - 2:
    slovar[x] = [input[i+1]]
    if input[i+2] - x <= 3:
      slovar[x].extend([input[i+2]])
  elif i < len(input) - 1:
    slovar[x] = [input[i+1]]
  else:
    slovar[x] = []






slovar_opcij = {}

def opcije(x): # get_memo
  if x in slovar_opcij:
    return slovar_opcij[x]
  else:
    r = st_opcij(x)
    slovar_opcij[x] = r
    return r

def st_opcij(zadnji_el):
  mozni = slovar[zadnji_el] # possible
  if len(mozni) == 3:
    return opcije(mozni[0]) + opcije(mozni[1]) + opcije(mozni[2])
  elif len(mozni) == 2:
    return opcije(mozni[0]) + opcije(mozni[1])
  elif mozni:
    return opcije(mozni[0])
  else:
    return 1

r = st_opcij(0) # 10578455953408