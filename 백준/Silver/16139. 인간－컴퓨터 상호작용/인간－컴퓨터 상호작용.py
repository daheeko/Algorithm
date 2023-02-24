import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

for _ in range(q):
    p = input().split()
    sub = s[int(p[1]) : int(p[2])+1]
    print(sub.count(p[0]))
