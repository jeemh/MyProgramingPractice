def solution(citations):
    answer = 0
    for i in range(len(citations)):
        h_index = len(citations)-i
        count = 0
        for j in range(len(citations)):
            if citations[j] >= h_index:
                count+=1
        if count >= h_index:
            return h_index
    return 0