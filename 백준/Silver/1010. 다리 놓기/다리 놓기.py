import sys
input = sys.stdin.readline

d = [[0]*31 for _ in range(31)]
for m in range(1, 31):
    d[m][1] = m
    for n in range(2, m+1):
        d[m][n] = (m-n+1) * d[m][n-1] / n

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(int(d[M][N]))