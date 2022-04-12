visited = [False] * 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8], 
    [1, 7]
]
def dfs(graph, v, visited): # DFS 메소드 정의 
    # 현재 노드 방문 처리 
    visited[v] = True # 방문 했으면 True 로 바꾸어 줌. 
    print(v, end=' ') # 방문한 노드 출력 
    for i in graph[v]: 
        if not visited[i]: # 방문하지 않았다면
            dfs(graph, i, visited)
dfs(graph, 1, visited)


n, m = map(int, input().split())

graph = []
for i in range(n): 
    graph.append(list(map(int, input())))
    
# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문 
def dfs(x, y): 
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<0 or x>n-1 or y<0 or y>m-1: 
        return False 
    # 현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 
        graph[x][y] = 1 
        # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출 
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True 
    return False 

result = 0 
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행 
        if dfs(i, j) == True: 
            result += 1 
print(result) # 정답 출력 


def permute(items): 
    results = []
    def dfs(items, done):
        # done이 완성된 순열이면 results에 넣는다 
        if not items:
            results.append(done)
        else:
            for i in range(len(items)): 
                dfs(items[0:i]+items[i+1:], done+[items[i]])
    
    dfs(items, [])
    return results

print(permute(['A', 'B']))
print(permute([1, 2, 3]))


def subsets(items):
    results = []
    def dfs(subset, i):
        if i == len(items):
            results.append(subset[:])
        
        else:
            # 인덱스 i가 있는 경우
            subset.append(items[i])
            dfs(subset, i+1)
            # 인덱스 i가 없는 경우
            subset.pop()
            dfs(subset, i+1)
    dfs([], 0)
    return results


print(subsets([]))
print(subsets([0]))
print(subsets([0,1]))
print(subsets([0,1,2]))

def house_num(map_str):
    graph = [list(map(int, k)) for k in map_str.split() if k]
    n = len(graph)
    visited = [[False]*n for _ in range(n)]
    ans = []
    
    def dfs(x, y):
        if (0<=x<=n-1) and (0<=y<=n-1) and not visited[x][y] and graph[x][y]==1:
            visited[x][y]=True # 방문 처리 
            
            a = dfs(x-1, y)
            b = dfs(x+1, y)
            c = dfs(x, y-1)
            d = dfs(x, y+1)
            
            return 1+a+b+c+d
        else: # 방문 할 수 없는 경우
            return 0 
        
    for x in range(n): 
        for y in range(n): 
            size = dfs(x, y)
            if size > 0: 
                ans.append(size)
    
    return sorted(ans)
    
    
    
map_str = """
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""

print(house_num(map_str))