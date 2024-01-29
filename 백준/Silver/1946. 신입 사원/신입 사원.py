import sys

testCase = int(sys.stdin.readline())
for _ in range(testCase):
    N = int(sys.stdin.readline())
    cnt = N
    volunteer = [None]*N
    for i in range(N):
        volunteer[i] = list(map(int,sys.stdin.readline().split()))
        volunteer[i].append(1)
    volunteer.sort()
    minScore = volunteer[0][1]
    for i in range(1,len(volunteer)):
        # print("<",volunteer[i][1], minScore,">")
        if volunteer[i][1] > minScore :
            volunteer[i][2] = 0 #면접 탈락
            cnt -= 1
        elif volunteer[i][1] < minScore:
            minScore = volunteer[i][1]
    volunteer = sorted(volunteer, key=lambda x: x[1])        
    minScore = volunteer[0][0]
    for i in range(1,len(volunteer)):
        if volunteer[i][0] > minScore and volunteer[i][2]:
            volunteer[i][2] = 0 #면접 탈락
            cnt -= 1
        elif volunteer[i][0] < minScore:
            minScore = volunteer[i][0]
    print(cnt)
    #print(volunteer)