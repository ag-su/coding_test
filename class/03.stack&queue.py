def is_valid_parentheses(s): 
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char not in table: # 열린 괄호인지 체크 
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0 


def wheather(T): 
    result = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)
    return result          


def remove_dups(s):
    stack = []
    for i in s: 
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)            
    return "".join(stack)

print(remove_dups("caaa"))
print(remove_dups("accab"))
print(remove_dups("baccaaac"))


#############################
def rain_trap(heights):
    stack = [] # 왼쪽기둥, 웅덩이 저장  
    volume = 0
    
    for i in range(len(heights)):
        while stack and heights[stack[-1]] < heights[i]:
            cur = stack.pop()
            if not stack: # 왼쪽 블럭이 없다
                break     # cur 왼쪽에는 기둥이 하나 있어야 물이 고일 수 있음
            left = stack[-1]
            if heights[left] == heights[cur]:
                continue # 왼쪽으로 한번 더 가 봄 
            
            # 왼쪽 기둥 찾음 
            right = i
            
            d = right - left - 1
            h = min(heights[left], heights[right]) - heights[cur]
            volume += d*h
            #print(f"i:{i}, cur:{cur}, d:{d}, h:{h}")
        
        stack.append(i)
        
    return volume
    
# 아래는 수정하지 마시오.
print(rain_trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(rain_trap([0,4,0,0,1,0,3]))


####################################
from collections import deque

def printer_order(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)]) # i: 처음 시작 위치 , p: 우선순위
    
    sorted_p = sorted(priorities) # 오름차순 정렬
    answer = 0
    
    while True: 
        # 큐에서 문서 꺼내기 
        i, p = queue.popleft()
        if queue and p < sorted_p[-1]: # 대기열에 더 높은 문서가 있다. 
            queue.append((i, p))  # 뒤에 저장 
        else:
            answer += 1 
            sorted_p.pop()
            if i == location: 
                return answer 
        
print(printer_order([2, 1, 3, 2], 2))
print(printer_order([2, 1, 3, 2], 1))
print(printer_order([2, 1, 3, 2], 3))
print(printer_order([1, 1, 9, 1, 1, 1], 0))

            
    