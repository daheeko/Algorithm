import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
min = price[0]
answer = 0

for i in range(n-1):
    if price[i] <= min:
        min = price[i]
    answer += min*dist[i]
print(answer)