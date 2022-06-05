def solution(nums):     
    catch_num = len(nums) / 2 # 잡을 수 있는 폰켓몬 개수 
    type_num =  len(set(nums)) # 종류의 개수 
    if catch_num < type_num:
        return catch_num
    return type_num

# 다른 사람 풀이 
def solution(ls):
    return min(len(ls)/2, len(set(ls)))