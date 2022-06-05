##### 1. BFS 소스코드 예제 
from collections import deque 

# BFS 메서드 정의 
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리 
    visited[start] = True 
    # 큐가 빌 때까지 반복 
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기 
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

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

visited = [False] * 9

bfs(graph, 1, visited)

##### 2. 미로 탈출 
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                continue
                
            # 벽일 경우 무시 
            if graph[nx][ny] == 0:
                continue
                
            # 해당 노드를 처음 방문하는 경우에만 최단 거러ㅣ 기록 
            if graph[nx][ny]==1 and not (nx==0 and ny==0):
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx, ny))
            
    return graph[n-1][m-1] 

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
print(bfs(0, 0))


##### 3. 백준 토마토 문제 
from collections import deque
def tomato(input_str):
    grid = [[int(x) for x in k.split()] for k in input_str.split('\n') if k]
    n = len(grid)     
    m = len(grid[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
           
    queue = deque()       
           
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1:
                queue.append((x, y))
                
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0<=nx<n and 0<=ny<m) and (grid[nx][ny]==0):
                grid[nx][ny] = grid[x][y]+1
                queue.append((nx, ny))

    max_value = 0 
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 0: 
                return -1 
            if max_value < grid[x][y]:
                max_value = grid[x][y]
    
    return max_value-1
                
        
# 아래는 수정하지 마시오.
input_str = """
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""
print(tomato(input_str))

input_str = """
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
"""
print(tomato(input_str))

input_str = """
1 0 0
0 -1 0
0 -1 0
0 0 1
"""
print(tomato(input_str))

input_str = """
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""
print(tomato(input_str))

input_str = """
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0
"""
print(tomato(input_str))

input_str = """
1 -1
-1 1
"""
print(tomato(input_str))

##### 4. 술래잡기 
from collections import deque 
def hide_and_seek(N, k): 
    max_N = 100000 
    
    visited = set([N])
    queue = deque([[N, 0]]) # (노드, 시작 노드에서 해당 노드까지 걸리는 시간)
    
    def enqueue(n, time):
        if (0<=n<=max_N) and (n not in visited):
            visited.add(n) # 방문표시 
            queue.append([n, time])
            
    while queue:
        new_N, time = queue.popleft()
        
        if new_N == k:
            return time 
        
        else: 
            for x in [new_N-1, new_N+1, new_N*2]:
                enqueue(x, time+1)
        
    return None 
    
# 아래는 수정하지 마시오.
print(hide_and_seek(1, 4))
print(hide_and_seek(5, 17))
print(hide_and_seek(5, 18))
print(hide_and_seek(1, 10000))