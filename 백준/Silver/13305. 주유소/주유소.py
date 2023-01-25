import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
temp = []
min = price[0]
for i in range(n-1):
    if price[i] <= min:
        min = price[i]
    temp.append(min)
result = sum([d*p for d, p in zip(dis, temp)])
print(result)