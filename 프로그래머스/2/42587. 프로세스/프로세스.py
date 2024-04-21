def solution(priorities, location):
    count = 0
    answer = 0
    copyArr = []
    for i in range(len(priorities)):
        copyArr.append([priorities[i], i])
    priorities = sorted(priorities, reverse = True)
    
    while True:
        if priorities[0] == copyArr[0][0]:
            count += 1
            if(copyArr[0][1] == location):
                break;
            priorities.pop(0)
            copyArr.pop(0)
        else:
            copyArr.append(copyArr.pop(0))
            
    return count