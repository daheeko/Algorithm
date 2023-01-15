from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
D = list(map(int, input().split()))
myD = deque()

# 새 값 넣어주기
for i in range(N):
    # 덱에 값 있는데 맨 오른쪽 값이 들어올 값보다 크면 삭제
    while myD and myD[-1][1] > D[i]:
        myD.pop()
    # (idx, 값) 형태로 저장
    myD.append((i, D[i]))  
    # 인덱스가 범위 벗어나면 삭제
    if i - myD[0][0] >= L:  
        myD.popleft()
    print(myD[0][1], end=" ")  # 최솟값==덱 첫 번째 값