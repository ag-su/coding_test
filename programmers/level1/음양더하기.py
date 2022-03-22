def solution(absolutes, signs):
    lst_num = [num if sign else -1*num for num, sign in zip(absolutes, signs)]        
    return sum(lst_num)

# 내적 (비슷한 코드여서 같은 파일에 작성)
def solution(a, b):
    return sum(x*y for x, y in zip(a, b))