##### 1. 삽입정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)


##### 2. 퀵 정렬 - 일반적인 방식
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return 
    
    pivot = start # 피벗은 첫 번째 원소 
    left = start + 1 
    right = end 
    while (left <= right): 
        #  피벗보다 큰 데이터를 찾을 때 까지 반복 
        while (left<=end and array[left] <= array[pivot]):
            left += 1 
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while (right>start and array[right] >= array[pivot]):
            right -= 1 
        if (left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체 
            # left가 right보다 크단 소리는 left와 right를 바꿀 필요가 없다는 소리다. 
            # -> pivot을 교체해 주어야 한다. 
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
            array[left], array[right] = array[right], array[left]
          
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
        
quick_sort(array, 0, len(array)-1)
print(array)


##### 3. 퀵 정렬: 파이썬의 장점을 살린 방식 
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    #  리스트가 하나 이하의 원소만을 담고 있다면 종료 
    if len(array) <= 1: 
        return array 
    pivot = array[0] # 피벗은 첫 번 째 원소 
    tail = array[1:] # 피벗을 제외한 리스트 
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분 
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분 
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환 
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


##### 4, 계수 정렬 
# 안정 계수 정렬 (stable counting sort)
def counting_sort_stable(array):
    results = [None] * len(array)
    count = [0] * (max(array) + 1) # 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
    
    for i in range(len(array)): 
        count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가 
    
    for i in range(len(count)-1):
        count[i+1] += count[i] # 누적 개수를 구한다. 
        
    for i in reversed(range(len(array))):
        count[array[i]] -= 1 # array[i]가 위치할 인덱스 값이 count[array[i]]에 들어있도록 값을 1 감소시킨다. 
        results[count[array[i]]] = array[i]
        
    return results

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print(counting_sort_stable(array))


##### 5. 특정 자리수를 기준으로 하는 계수 정렬 
def counting_sort_by_digit(array, digit):
    base = 10 # 10진법 
    
    def get_digit_number(num, digit): # 특정 자리수에 위치한 정수를 리턴하는 함수 
        return (num // (base ** (digit-1))) % base 
    
    results = [None] * len(array)
    count = [0] * base 
    
    for i in range(len(array)): 
        count[get_digit_number(array[i], digit)] += 1 
        
    for i in range(base-1):
        count[i+1] += count[i]
        
    for i in reversed(range(len(array))): 
        count[get_digit_number(array[i], digit)] -= 1 
        results[count[get_digit_number(array[i], digit)]] = array[i]
        
    return results 


##### 6. 기수 정렬
def radix_sort(array):
    max_digit = len(str(max(array))) # 자릿수 파악 
    
    for i in range(1, max_digit+1): # 1의 자리부터 계수 정렬을 수행한다. 
        array = counting_sort_by_digit(array, i)
        
    return array 


print(radix_sort([123, 1, 2, 3, 12, 23, 15, 257, 214, 999]))



##### 7. 두 배열의 원소 교체 
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k): 
    if a[i] < b[i]: 
        a[i], b[i] = b[i], a[i]
        
    else: 
        break 
        
print(sum(a))


##### 8. 기수정렬 복습
def counting_sort_by_digit(array, digit): # 예, digit == 2 -> 10의 자리를 기준으로 정렬
    base = 10 # 10진법

    def get_digit_number(num, digit): # 특정 자리수에 위치한 정수를 리턴하는 함수
        return (num // (base ** (digit - 1))) % base

    results = [None] * len(array)
    count = [0] * base

    for i in range(len(array)): # 개수 구하기
        count[get_digit_number(array[i], digit)] += 1
   
    for i in range(base-1): # 누적 개수 구하기
        count[i+1] += count[i]

    for i in reversed(range(len(array))):
        count[get_digit_number(array[i], digit)] -= 1
        results[count[get_digit_number(array[i], digit)]] = array[i]   
    
    return results



def radix_sort(array):
    max_digit = len(str(max(array)))

    for i in range(1, max_digit+1): 
        array = counting_sort_by_digit(array, i)
        print(f"sort by {10**(i-1)}")
        for x in array: 
            print(x)
        print()

    return array

        
#아래는 수정하지 마시오
data = [123, 401, 210, 113, 124, 784, 296, 472, 882, 251, 902, 943]
print(radix_sort(data))
