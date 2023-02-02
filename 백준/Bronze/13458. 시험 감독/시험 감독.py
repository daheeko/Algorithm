n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
result = len(a)

tmp = [i-b for i in a if i-b > 0]
for i in tmp:
    if i%c == 0:
        result += i//c
    else:
        result += (i//c + 1)
print(result)