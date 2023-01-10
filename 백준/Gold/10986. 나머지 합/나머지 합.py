import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n  # 부분 합 배열
S[0] = A[0] 
numR = [0] * m  # 나머지 값이 같은 인덱스 개수 저장 배열
result = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m  # 나머지 계산
    if remainder == 0:
        result += 1
    numR[remainder] += 1  

for i in range(m):
    if numR[i] > 1:
        result += (numR[i] * (numR[i]-1) // 2)  # nC2 계산

print(result)

