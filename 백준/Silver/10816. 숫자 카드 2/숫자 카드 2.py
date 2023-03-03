import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

dic = {}
for a in arr:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1


print(" ".join("0" if x not in dic else str(dic[x]) for x in nums))