def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)

    # 도난 당하고 여벌 체육복을 가져온 학생 제거, + 1 
    for num in lost[:]: 
        if num in reserve: 
            answer += 1 
            reserve.remove(num)
            lost.remove(num)

    for num in lost[:]:         
        if (num-1 in reserve): # num-1 이 reserve에 있으면   
            answer += 1 
            reserve.remove(num-1)

        elif (num+1 in reserve): # num+1 이 reserve에 있으면 
            answer += 1 
            reserve.remove(num+1)

    return answer


# 참고할 만한 풀이 
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)