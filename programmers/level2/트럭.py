from collections import deque 
def solution(bridge_length, weight, truck_weights):
    queue_bridge = deque([0]*bridge_length) # 다리 길이만큼 만들어 놓음 
    n = 0
    time = 0
    bridge_weight = 0

    while n < len(truck_weights):
        time += 1 # 시간 추가 
        truck = queue_bridge.popleft() # 다리 첫번째 빼기
        if truck > 0: 
            bridge_weight -= truck

        if bridge_weight+truck_weights[n] <= weight: 
            queue_bridge.append(truck_weights[n]) # 다리에 트럭 추가 
            bridge_weight += truck_weights[n]
            n += 1 

        else: 
            queue_bridge.append(0) # 0 추가 (길이 맞추기)


    return time + bridge_length