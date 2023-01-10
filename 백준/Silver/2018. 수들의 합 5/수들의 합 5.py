import sys
input = sys.stdin.readline

n = int(input())
sum, cnt = 1, 1  # n 자체는 더할 필요 없이 n 이니까 cnt 1부터 시작
start, end = 1, 1  # 인덱스

while end != n:  # 끝에 도달하기 전까지
    if sum == n:
        cnt += 1
        # 새로운 해 찾기
        end += 1
        sum += end
    elif sum > n:  # 더한 값이 커지면
        sum -= start
        start += 1  # start 오른쪽 이동 == 왼쪽 거 빼는 효과
    else:  # 더한 값이 작아지면
        end += 1  # end 오른쪽 이동 == 오른쪽 거 더하는 효과
        sum += end
    
print(cnt)
