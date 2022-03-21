# 문제 1
def maxProfit(prices):
    result = 0
    for i in range(len(prices)-1): 
        gap = prices[i+1] - prices[i]
        if gap > 0: 
            result += gap  
    return result
                        
# 아래는 수정하지 마시오.
prices01 = [7,1,5,3,6,4]
print(maxProfit(prices01))


# 문제 2 
def findContentChildren(g, s):
    g.sort()
    s.sort() 
    
    i = 0 # 아이 인덱스 
    j = 0 # 쿠키 인덱스 

    while (i < len(g)) and (j < len(s)): 
        if g[i] <= s[j]: # i번째 아이가 만족 
            i += 1 
            j += 1 
        else: 
            j += 1 
            
    return i   

# 아래는 수정하지 마시오.
print(findContentChildren([1,2,3], [1,1]))
print(findContentChildren([1,2], [1,2,3]))
print(findContentChildren([2,3,4], [1,5,3,1]))