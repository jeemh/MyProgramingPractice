import sys
def sortAndDropOut(sortCriteria, criteriaForElimination, volunteer):

    howManyDropOut = 0 
    volunteer = sorted(volunteer, key=lambda x: x[sortCriteria]) #기준으로 정렬
    minScore = volunteer[0][criteriaForElimination] #정렬된 스코어중 나머지 스코어로 비교하기위해 초기값을 0번째 지원자로 설정

    for i in range(1,len(volunteer)):
        if volunteer[i][criteriaForElimination] > minScore and volunteer[i][2]:
            volunteer[i][2] = 0 #면접 탈락
            howManyDropOut += 1

        elif volunteer[i][criteriaForElimination] < minScore: #최고등수 초기화
            minScore = volunteer[i][criteriaForElimination]
    
    return howManyDropOut

testCase = int(sys.stdin.readline())
for _ in range(testCase):
    N = int(sys.stdin.readline())
    cnt = N
    volunteer = [None]*N
    for i in range(N):
        volunteer[i] = list(map(int,sys.stdin.readline().split()))
        volunteer[i].append(1)
    cnt -= sortAndDropOut(0,1,volunteer)
    cnt -= sortAndDropOut(1,0,volunteer)
    # volunteer.sort()
    # minScore = volunteer[0][1]
    # for i in range(1,len(volunteer)):
    #     if volunteer[i][1] > minScore :
    #         volunteer[i][2] = 0 #면접 탈락
    #         cnt -= 1
    #     elif volunteer[i][1] < minScore:
    #         minScore = volunteer[i][1]
    # volunteer = sorted(volunteer, key=lambda x: x[1])        
    # minScore = volunteer[0][0]
    # for i in range(1,len(volunteer)):
    #     if volunteer[i][0] > minScore and volunteer[i][2]:
    #         volunteer[i][2] = 0 #면접 탈락
    #         cnt -= 1
    #     elif volunteer[i][0] < minScore:
    #         minScore = volunteer[i][0]
    print(cnt)
    #print(volunteer)