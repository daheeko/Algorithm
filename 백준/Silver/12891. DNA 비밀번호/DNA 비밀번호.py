import sys
input = sys.stdin.readline

checklist = [0] * 4  # 규칙 ('A', 'C', 'G', 'T')
now = [0] * 4  # 현재 sub문자열에서 각 문자 개수
flag = 0  # 규칙 충족 수치 (4여야 만족)

# 문자 추가될 때
def addlist(c):
    global checklist, now, flag
    if c == 'A':
        now[0] += 1
        if checklist[0] == now[0]:
            flag += 1
    elif c == 'C':
        now[1] += 1
        if checklist[1] == now[1]:
            flag += 1
    elif c == 'G':
        now[2] += 1
        if checklist[2] == now[2]:
            flag += 1
    elif c == 'T':
        now[3] += 1
        if checklist[3] == now[3]:
            flag += 1

def removelist(c):
    global checklist, now, flag
    if c == 'A':
        if checklist[0] == now[0]:
            flag -= 1
        now[0] -= 1
    elif c == 'C':
        if checklist[1] == now[1]:
            flag -= 1
        now[1] -= 1
    elif c == 'G':
        if checklist[2] == now[2]:
            flag -= 1
        now[2] -= 1
    elif c == 'T':
        if checklist[3] == now[3]:
            flag -= 1
        now[3] -= 1

#--메인
s, p = map(int, input().split())
dna = input() # list(input().rstrip())
checklist = list(map(int, input().split()))  # a c g t
result = 0

# 이미 0인 조건 챙겨주기
for i in range(4):
    if checklist[i] == 0:
        flag += 1

# 제일 앞 부분문자열 
for i in range(p):
    addlist(dna[i])  # 문자 개수 셋팅

if flag == 4:
    result += 1  # 조건 충족 확인

for i in range(p, s):  # 첫 부분 문자열은 확인 완료, 그 뒤부터
    j = i - p  # start idx
    addlist(dna[i])  # 뒤쪽 문자는 추가
    removelist(dna[j])  # 앞쪽 문자는 삭제
    if flag == 4:  # 업데이트된 문자열이 조건 충족 시
        result += 1

print(result)
