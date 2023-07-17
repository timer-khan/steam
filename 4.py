s = input().split()

alph = dict()
for el in s:
    if el not in alph:
        alph[el] = 1
    else:
        alph[el] += 1

print(alph)
print(alph.keys())
print(alph.values())

