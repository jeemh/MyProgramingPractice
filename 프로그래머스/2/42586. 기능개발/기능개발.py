def solution(progresses, speeds):
    answer = []
    progresses.insert(0, -1)
    flag = True
    while(flag):
        count = 0
        for i in range(1, len(progresses)):
            if progresses[i] != -1:
                progresses[i] += speeds[i-1]
            if (progresses[i-1] == -1) and (progresses[i] >= 100):
                count += 1
                progresses[i] = -1
                if i == len(progresses)-1:
                    flag = False
        if count > 0:
            answer.append(count)
    return answer