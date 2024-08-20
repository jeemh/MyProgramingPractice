def solution(jobs):
    time = 0
    sum = 0
    diskLen = len(jobs)
    jobs.sort(key=lambda x:x[1])
    while len(jobs) > 0:
        for i in range(len(jobs)):
            if time >= jobs[i][0]:
                sum += time - jobs[i][0] + jobs[i][1]
                time += jobs[i][1]
                jobs.pop(i)
                break
            if i == len(jobs)-1:
                time += 1
            
    return sum//diskLen