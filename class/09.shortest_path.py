##### 힙 라이브러리 사용 예제: 최소 힙  
import heapq 

def heapsort(iterable):
    h = [] # 리스트 선언 
    result = [] # 최종적으로 정렬된 리스트 
    # 모든 원소를 차례대로 힙에 삽입 
    for value in iterable:
        heapq.heappush(h, value) # value: 우선순위 
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 우선순위 대로 pop 된다
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)



##### 2. 다익스트라 알고리즘
import heapq
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정 

def dijkstra(graph, start):
    n = len(graph) # 노드의 개수 
    distance = {k:INF for k in graph}
    distance[start] = 0
    
    q = [] # 최조힙 저장 변수 
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입 
    heapq.heappush(q, (0, start))  # 거리, 노드 
    
    while q: # 큐가 비어있지 않다면 
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        dist, now = heapq.heappop(q) # now: 현재 방문처리 중인 노드 
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 
        # 현재 꺼낸 노드의 거리보다 distance에서 더 작은 거리로 저장되어 있다는 것은 
        # 우선순위 큐에서 한번 꺼낸 적이 있다는 소리이기 때문에  
        # 왜냐면 우선순위가 더 작은 튜플이었기 때문에 먼저 탈출했다는 소리
        if distance[now] < dist: 
            continue 
            
        # 현재 노드와 연결된 다른 인접한 노드들을 확인 
        for node, weight in graph[now]:
            cost = dist + weight # 1~현재노드 + 현재노드~인접노드
            # 현재 노드를 거쳐서, 인접 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
            
    return distance