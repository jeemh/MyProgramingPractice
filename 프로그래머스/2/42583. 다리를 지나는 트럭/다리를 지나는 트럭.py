def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0] * bridge_length
    queue_pointer = 0
    truck_weights_pointer = 0
    weight_sum = 0
    while(len(truck_weights) > truck_weights_pointer):
        if queue[queue_pointer]>0:
            weight_sum -= queue[queue_pointer]
        queue_pointer += 1
        if (weight_sum + truck_weights[truck_weights_pointer]) <= weight:
            weight_sum += truck_weights[truck_weights_pointer]
            queue.append(truck_weights[truck_weights_pointer])
            truck_weights_pointer += 1
        else:
            queue.append(0)
        answer += 1
    answer += len(queue[queue_pointer:])

    return answer