import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D = list(map(int, input().split()))
S = [0] * (N+1)
for i in range(N):
    S[i+1] = S[i] + D[i]

for i in range(M):
    i, j = map(int, input().split())
    result = S[j] - S[i-1]
    print(result)