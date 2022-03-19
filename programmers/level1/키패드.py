import math

def solution(numbers, hand):
    dict_pos = {1: (0, 0), 2: (0, 1), 3: (0, 2), 
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2), 
                0: (3, 1), }

    now_pos_l = (3, 0) 
    now_pos_r = (3, 2)
    answer = ''
    
    for num in numbers: 
        if num in [1, 4, 7]:
            now_pos_l = dict_pos[num]
            answer += 'L'    
            
        elif num in [3, 6, 9]: 
            now_pos_r = dict_pos[num]
            answer += 'R'
            
        else:
            now = dict_pos[num]
            dis_l = math.sqrt(abs(now_pos_l[0] - now[0]) + abs(now_pos_l[1] - now[1]))
            dis_r = math.sqrt(abs(now_pos_r[0] - now[0]) + abs(now_pos_r[1] - now[1]))

            if dis_l < dis_r: 
                answer += 'L'
                now_pos_l = dict_pos[num]
            elif dis_l > dis_r:
                answer += 'R'
                now_pos_r = dict_pos[num]
            else: 
                answer += hand[0].upper()
                if hand == 'left': 
                    now_pos_l = dict_pos[num]
                else: 
                    now_pos_r = dict_pos[num]

    return answer
