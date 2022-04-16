from collections import deque
def solution(people, limit):
    answer = 0
    queue = deque(sorted(people)) 

    while len(queue)>=2:
        # 현재 가장 가벼운 + 현재 가장 무거운 
        if queue[0] + queue[-1] <= limit: 
            queue.popleft()
            queue.pop() 
            answer += 1 
        else: 
            queue.pop() 
            answer += 1

    return answer + len(queue)