import sys
input = sys.stdin.readline

N = int(input())
# sum = 0
# for n in input().rstrip():
#     sum += int(n)
# print(sum)

arr = map(int, input().rstrip())
print(sum(arr))