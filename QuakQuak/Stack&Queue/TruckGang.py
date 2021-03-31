def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    bridge = list()
    print(truck_weights.extend(2))
    for truck in truck_weights.extend(2):
        bridge.append(truck)
        cur_weight+=truck
        if len(bridge) < bridge_length:
            if cur_weight < weight:
                answer+=1
            else:
                answer+=(bridge_length-len(bridge)+1)
                bridge.remove(truck)
                cur_weight-=truck
        elif len(bridge) >= bridge_length:
            if cur_weight > weight:
                answer+=(bridge_length-len(bridge)+2)
                pop = bridge.pop(0)
                cur_weight-=pop
            else:
                answer += 1
    return answer

print(solution(2,10,[7,4,5,6]))
