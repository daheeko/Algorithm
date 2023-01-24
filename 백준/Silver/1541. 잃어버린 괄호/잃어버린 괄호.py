import sys
input = sys.stdin.readline

mdx =  input().rstrip()
result = 0
if '-' not in mdx:  # 10+20 / 20  
    lst = list(map(int, mdx.split("+")))
    result = sum(lst)
else:
    lst = mdx.split('-')  # ['10', '1+10', '19]
    for idx, m in enumerate(lst):
        temp = sum(list(map(int, m.split("+"))))
        if idx == 0:
            result += temp
        else:
            result -= temp
print(result)