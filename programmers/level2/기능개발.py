import math
def solution(progresses, speeds):
    answer = []
    day_list = []
    for progress, speed in zip(progresses, speeds): 
        day_list.append(math.ceil((100-progress) / speed))
        
    while True: 
        count = 1                         
    
        if len(day_list) == 0:
            break
        
        pop_num = day_list.pop(0)
        for _ in range(len(day_list)):
            if pop_num >= day_list[0]:
                day_list.pop(0)
                count += 1
            else:
                break

        answer.append(count)
        
    return answer


import math
def solution(progresses, speeds):
    answer = []
    stack = []  
    
    for p, s in zip(progresses, speeds): 
        day = math.ceil((100-p)/s)
        cnt = 0 
        while stack and stack[-1] < day and stack[0] < day:  
            stack.pop()
            cnt += 1 
            
        if cnt > 0:
            answer.append(cnt)
    
        stack.append(day)   
        
    return answer + [len(stack)]