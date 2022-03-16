# 나의 풀이 
def solution(lottos, win_nums):
    answer = [0, 0]
    dic_lotto = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    correct_num = 6 - len(set(win_nums) - set(lottos))
    num_0 = lottos.count(0)
    
    max_rank_num = correct_num + num_0
    min_rank_num = correct_num
    
    answer[0] = dic_lotto[max_rank_num]
    answer[1] = dic_lotto[min_rank_num]

    
    return answer

# 고수의 풀이 
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

# 고수의 풀이 2
def solution(lottos, win_nums):
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]