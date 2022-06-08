##### 1. 피보나치 수열 - 탑다운 
d = [0] * 100 

def fibo(x):
    # 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산한 적 있는 문제라면 그대로 반환 
    if d[x] != 0:
        return d[x]
    
    # 아직 계산하지 않은 문제라면 점화식에 따라서 결과 반환 
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


##### 2. 피보나치 수열 - 바텀업
# dp 테이블 초기화 
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1 
d[1], d[2] = 1, 1 
n = 99 

# 피보나치 함수 반복문으로 구현 (바텀업 다이나믹 프로그래밍)
for i in range(3, n+1): 
    d[i] = d[i-1] + d[i-2]
    
print(d[n])



##### 3. 피보나치 수열 - 메모이제이션 동작 분석 
d = [0] * 7

def fibo(x):
    print('f(' + str(x) + ')', end='')
    if x == 1 or x == 2:
        return 1 
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

fibo(6)  # f(6)f(5)f(4)f(3)f(2)f(1)f(2)f(3)f(4)


##### 4. 개미전사 
# 정수 n을 입력받기 
n = int(input())

# 모든 식량 정보 입력 받기 
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화 
d = [0] * n 

# 다이나믹 프로그래밍 진행 (바텀 업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n): 
    d[i] = max(d[i-1], d[i-2]+array[i])
    
print(d[-1])



##### 6. 1로 만들기 
def make_one(n):
    d = [0] * (n+1)
    
    for i in range(2, n+1): 
        c = [d[i-1]]
        for j in [2, 3, 5]:
            if i%j == 0:
                c.append(d[i//j])
                
        d[i] = min(c) + 1 
        
    return d[n]


print(make_one(5))
print(make_one(26))
print(make_one(111))



##### 7. 화폐 개수 
def change_coins(coins, amount):
    INF = 10001
    d = [INF] * (amount+1)
    d[0] = 0 
    
    for i in range(1, amount+1): 
        for coin in coins:
            if i>=coin:
                d[i] = min(d[i], d[i-coin]+1)
    
    return d[-1] if d[-1]<INF else -1
    
    
print(change_coins([2,5,8], 7))
print(change_coins([2,5], 101))
print(change_coins([2,5,9], 3))


##### 8. 2차원 dp, 화폐 개수
def change_coins2(amount, coins):
    d = [[1]+[0]*amount for _ in range(len(coins)+1)]
    
    for i in range(1, len(coins)+1):
        for j in range(1, amount+1):
            k = coins[i-1]
            if j>=k:
                d[i][j] = d[i-1][j] + d[i][j-k]
            else:
                d[i][j] = d[i-1][j]
    
    return d[-1][-1]


# 아래는 수정하지 마시오.
print(change_coins2(3, [1,2]))
print(change_coins2(5, [1,2,5]))
print(change_coins2(7, [1,2,5]))