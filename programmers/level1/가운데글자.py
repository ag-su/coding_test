
def solution(s):
    return s[len(s)//2] if len(s)%2!=0 else s[int(len(s)/2)-1:int(len(s)/2)+1]

# 다른 사람 풀이 
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
