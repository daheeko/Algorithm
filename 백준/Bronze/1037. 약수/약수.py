import sys

cnt = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort() 

if cnt%2 == 0:
    idx = cnt // 2
    result = data[idx-1] * data[idx]
else:
    idx = cnt // 2
    result = data[idx] ** 2
print(result)