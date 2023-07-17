a = [int(el) for el in input().split()]
if (a[0] * a[2]) % a[1] == 0:
    print(a[0] * a[2] // a[1])
else:
    print(a[0] * a[2] // a[1] + 1)
