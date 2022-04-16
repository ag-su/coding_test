def solution(number, k):
    stack = [] # 더 높은 숫자 만나면 처리 
    for i, num in enumerate(number): 
        while stack and stack[-1] < num and k > 0: 
            k -= 1
            stack.pop() 
        stack.append(num)
        
    if k != 0: 
        stack = number[:-k]

    return ''.join(stack)