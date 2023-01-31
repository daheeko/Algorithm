n = int(input())
d = [0] * 100001
sqrt = [i*i for i in range(1, int(n**0.5)+1)]  # 제곱수만 저장
for i in range(1,n+1):
    temp = []
    for j in sqrt:
        if j > i:
            break
        temp.append(d[i-j] + 1)
    d[i] = min(temp)
print(d[n])