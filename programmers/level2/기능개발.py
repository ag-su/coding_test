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