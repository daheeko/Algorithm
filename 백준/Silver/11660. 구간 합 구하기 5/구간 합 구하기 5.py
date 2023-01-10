import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0]*(n+1)]  # [[0, 0, 0,..]] 인덱스 맞추기용 0행 
D = [[0]*(n+1) for _ in range(n+1)]  # [[0,0,.. ], [0,0,..], ...]

for i in range(n):
    a = [0] + list(map(int, input().split()))  # 인덱스 맞추기용 0열 추가
    A.append(a)

# 합 배열 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 구간 합 구하기
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)