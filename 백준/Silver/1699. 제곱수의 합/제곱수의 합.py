n = int(input())
d = [0] * 100001
for i in range(1,n+1):
    d[i] = i   # 1^2으로 i를 만들 때의 개수(최댓값)
    for j in range(1, i):
        if j**2 > i:
            break
        d[i] = min(d[i], 1 + d[i - j**2])
print(d[n])