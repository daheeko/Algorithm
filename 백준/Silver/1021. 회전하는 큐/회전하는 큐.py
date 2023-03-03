N, M = map(int, input().split())
Q = [*range(1, N+1)]
idx, cnt=0, 0
for i in list(map(int, input().split())):
    cnt += min(abs(idx-Q.index(i)), len(Q)-abs(idx-Q.index(i)))
    idx = Q.index(i)
    del Q[Q.index(i)]
print(cnt)