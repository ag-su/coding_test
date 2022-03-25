def solution(numbers):
    answer = set()
    cnt = len(numbers)-1
    j = 1
    for num in numbers: 
        for i in range(cnt):
            i += j
            answer.add(num+numbers[i])
        cnt-=1
        j+=1
    return sorted(list(answer))


# 다른 사람 풀이: 내 코드 깔끔 버전 
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


# 다른 사람 풀이: combinations 사용 
from itertools import combinations
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))