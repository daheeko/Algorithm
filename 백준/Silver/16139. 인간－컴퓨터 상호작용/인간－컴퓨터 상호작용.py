import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

count = [[0] * 26 for _ in range(len(s))]  # 구간 별로 각 알파벳 개수 셀 배열
count[0][ord(s[0]) - 97] = 1
for i in range(1, len(s)):
    count[i][ord(s[i]) - 97] = 1  # 문자열 (i, i번째 알파벳) 위치 1로 초기화
    for j in range(26):
        count[i][j] += count[i-1][j]  # 직전까지의 알파벳 개수 반영해주기

for _ in range(q):
    a, l, r = input().split()
    l, r = map(int, [l, r])
    if l > 0:
        print(count[r][ord(a) - 97] - count[l-1][ord(a) - 97])
    else:
        print(count[r][ord(a) - 97])
