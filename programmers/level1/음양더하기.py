def solution(absolutes, signs):
    lst_num = [num if sign else -1*num for num, sign in zip(absolutes, signs)]        
    return sum(lst_num)