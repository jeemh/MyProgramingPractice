firstString = input()
secondString = input()

firstLen = len(firstString) + 1
secondLen = len(secondString) + 1

LCS = [[0] * secondLen for _ in range(firstLen)]
#print(LCS[0])
for i in range(1,firstLen):
    for j in range(1,secondLen):
        if firstString[i-1] == secondString[j-1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
    #print(LCS[i])
print(LCS[firstLen-1][secondLen-1])

# 참고 블로그 : https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence