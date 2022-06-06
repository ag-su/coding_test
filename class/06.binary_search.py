##### 1. 이진탐색 소스코드 (재귀적 구현)
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2 
    # 찾은 경우 중간점 인덱스 반환 
    if array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
    
    
# n (원소의 개수) 과 target (찾고자 하는 값)을 입렵 받기 
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기 
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력 
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다. ")
else:
    print(result + 1)


###### 2. 이진 탐색 소스코드 (반복문 구현)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2 
        # 찾은 경우 중간점 인덱스 반환 
        if array[mid] == target:
            return mid 
        
        elif array[mid] > target:
            end = mid - 1 
        
        else:
            start = mid + 1 
    return None 

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력 
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


##### 3. 이진탐색 라이브러리 bisect 
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4 

print(bisect_left(a, x))
print(bisect_right(a, x))



##### 4. bisect_left를 이용한 이진탐색 
from bisect import bisect_left, bisect_right

def search(nums, target):
    index = bisect_left(nums, target)
    
    if index < len(nums) and nums[index] == target:
        return index 
    else:
        return -1 
    
print(search([1, 2, 5, 6, 8, 9], 5))


##### 5. 정렬된 배열에서 특정 수의 개수 구하기 
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수 
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index 


n, x = map(int, input().split()) 
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0: 
    print(-1)
else:
    print(count)


##### 6. 떡볶이 떡 만들기 
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정 
start = 0 
end = max(array)

# 이진 탐색 수행 (반복적)
while (start<=end):
    total = 0 
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m: 
        end = mid - 1
    else:
        result = mid 
        start = mid + 1 
        
print(result)


##### 7. bisect_left 직접 구현하기 
def my_bisect_left(nums, target):
    start = 0 
    end = len(nums) - 1 
    
    
    while start<=end: 
        mid = (start + end) // 2 
        
        if nums[mid] >= target:
            end = mid - 1

        else: 
            start = mid + 1 
            
    return start
    
print(my_bisect_left([1], 3))
print(my_bisect_left([1,2,3], 3))
print(my_bisect_left([1,1,2,2,2,3], 2))


##### 8. 예산 요청 
def solve(demand, budget):
    start = 0 
    end = max(demand)
    result = 0 
    
    while start <= end:
        total = 0 # 지급한 예산의 합
        mid = (start+end)//2 # 상한액 (커트라인)
        
        for x in demand:
            if x > mid: # 요구한 금액이 상한액보다 큰 경우
                total += mid 
            else: # 상한을 넘지 않음 
                total += x
                
        if total > budget: 
            end = mid - 1 
            
        else:
            result = mid
            start = mid + 1 
            
    
    return result
            
# 아래는 수정하지 마시오.
print(solve([120, 110, 140, 150], 485))
print(solve([70, 80, 30, 40, 100], 450))



##### 9. 두 수 덧셈하여 타겟 값 만들기 - 부루트포스 (완전탐색)
def find_two_sum1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    pass

print(find_two_sum1([2, 7, 11, 15], 22))


##### 10. 두 수 덧셈하여 타겟 값 만들기 - 이진탐색
def find_two_sum2(nums, target):
    for i, v in enumerate(nums):
        left = i + 1
        right = len(nums) - 1
        expected = target - v
        
        while left <= right:
            mid = ( left + right ) // 2
            if nums[mid] < expected:
                left = mid + 1
            elif nums[mid] > expected:
                right = mid - 1
            else:
                return i, mid 

print(find_two_sum2([2, 7, 11, 15], 22))
