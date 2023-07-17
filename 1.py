h = [int(el) for el in input().split()]
if (h[0] >= h[1] and h[1] >= h[2] and h[2] >= h[3]) or \
    h[0] <= h[1] and h[1] <= h[2] and h[2] <= h[3]:
    print("YES")
else:
    print("NO")
