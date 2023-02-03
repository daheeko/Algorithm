n = int(input())
a = set(input().split())
m = int(input())
b = input().split()

answer = '\n'.join('1' if x in a else '0' for x in b)
print(answer)