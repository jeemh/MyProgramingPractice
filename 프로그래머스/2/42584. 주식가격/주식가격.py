def solution(prices):
    answer = []
    for i in range(len(prices)):
        flag = True
        for j in range(i,len(prices)):
            if(prices[i] > prices[j]):
                answer.append(j-i)
                flag = False
                break
        if flag:
            answer.append(len(prices)-1-i)
    return answer