from collections import deque
def solution(priorities, location):
    idx = deque([i for i in range(len(priorities))] ) # 인덱스 기억용 리스트
    deq = deque(priorities)
    answer = 0
    while location in idx:
        n = deq.popleft()
        if len(deq) == 0:
            answer += 1
            break
        if n >= max(deq):   # 제일 중요도 높으면
            idx.popleft()  # 인쇄
            answer += 1
        else:
            deq.append(n)
            idx.rotate(-1)
    
    
    return answer