def solution(prices):
    answer = [0]*len(prices)
    stack = [] # 가격이 떨어지지 않은 주식을 관리, 떨어진 가격을 만났을 때 처리해 줌 
    for i, cur in enumerate(prices): 
        while stack and prices[stack[-1]] > cur:
            pop_idx = stack.pop()
            answer[pop_idx] = i - pop_idx

        stack.append(i)

    # 처리되지 못한 주식 처리
    for idx in stack: 
        answer[idx] = len(prices)-1 - idx

    return answer