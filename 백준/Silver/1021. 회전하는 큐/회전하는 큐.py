import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
deq = deque([i for i in range(1, n+1)])
result = 0

for num in nums:
    idx = deq.index(num)
    front = idx
    back = len(deq) - idx
    while True:
        if deq[0] == num:  #
            deq.popleft()
            break
        else:
            if front <= back:  # 왼쪽 한 칸, 즉 앞에 애들을 뒤로
                deq.rotate(-1)
                front -= 1
                back += 1
            else:
                deq.rotate(1)
                front += 1
                back -= 1
            result += 1
print(result)