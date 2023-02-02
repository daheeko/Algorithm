n, m, k = map(int, input().split())
result = 0
g, b = False, False  # 남는 쪽이 True
while k != 0: 
    if n > 2*m:
        g, b = True, False
        n -= 1
    elif n < 2*m:
        g, b = False, True
        m -= 1        
    else:  # 같아졌으면 일단 여자 빼기
        n -= 1
    k -= 1
if n >= 2*m:
    result = m
else:
    result = n // 2  # 몫
    
print(result)