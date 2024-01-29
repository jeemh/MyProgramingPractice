import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

LCS = [1] * N
# print(LCS)
for i in range(1,N):
    maxNum = 1
    for j in range(i):
        if A[i] > A[j] :
            LCS[i] = max(LCS[i],LCS[j]+1)
    # LCS[i] = maxNum + 1
    # print(LCS)   
print(max(LCS))

#참고 블로그 : https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-11053%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC