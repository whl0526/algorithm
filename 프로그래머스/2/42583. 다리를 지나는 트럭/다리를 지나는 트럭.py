def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge_weight = 0
    
    while truck_weights:
        answer += 1
        
        bridge_weight -= bridge.pop(0)
        
        if bridge_weight + truck_weights[0] <= weight:
            t = truck_weights.pop(0)
            bridge.append(t)
            bridge_weight += t
        else:
            bridge.append(0)
            
    return answer + bridge_length  # 마지막 트럭이 다리를 지날 때까지의 시간 추가

        