T = int(input())
for tc in range(T):
    d = [0] * 11
    n = int(input())
    d[1], d[2], d[3] = 1, 2, 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] +d[i-3]
    print(d[n])