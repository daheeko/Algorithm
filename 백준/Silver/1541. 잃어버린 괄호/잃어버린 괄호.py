import sys
input = sys.stdin.readline

mdx =  input().rstrip()
result = 0

lst = mdx.split('-')  # ['10', '1+10', '19]
for idx, m in enumerate(lst):
    temp = sum(list(map(int, m.split("+"))))
    if idx == 0:
        result += temp
    else:
        result -= temp
print(result)