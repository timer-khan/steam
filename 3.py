from pprint import pprint

int(input())
s = input() # caadbbbbdacc
alph = ['a', 'b', 'c', 'd']
t = False
p = {
    "a": [],
    "b": [],
    "c": [],
    "d": [],
}
for i, el in enumerate(s):
    p[el].append(i)

for el in p.values():
    if not el:
        print(-1)
        t = True
        break
if not t:
    ans = []
    for i, el in enumerate(p.values()):
        d = []
        if i == 3:
            break
        for index_1 in el:
            r = 10000000
            b = -1
            for index_2 in list(p.values())[i + 1]:
                if abs(index_2 - index_1) < r:
                    r = abs(index_2 - index_1)
                    b = index_2
            d.append((index_1, b))
        ans.append(d)


    paths1 = []
    for el in ans[0]:
        for ell in ans[1]:
            if el[1] == ell[0]:
                paths1.append([el, ell])

    paths2 = []
    for el in ans[1]:
        for ell in ans[2]:
            if el[1] == ell[0]:
                paths2.append([el, ell])

    ans = []
    for el in paths1:
        for ell in paths2:
            if el[1] == ell[0]:
                ans.append([el[0], ell[1]])

    res = []
    for el in ans:
        m = sorted(el[0] + el[1])
        res.append(m[-1] - m[0] + 1)
    print(min(res))
