import sys 
from queue import PriorityQueue
 
N = int(sys.stdin.readline())

endtime = 0
meetings = [None]*N
que = PriorityQueue() #우선순위큐

for i in range(N): #입력받는 부분
    meetings[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N): #우선순위큐에 회의시간이 먼저 시작하는 회의를 우선순위로 넣어둠
    que.put((meetings[i][0],meetings[i])) 
for i in range(N): #우선순위큐에서 빼서 시작시간이 작은 순서대로 정렬
    meetings[i] = que.get()[1] 
for i in range(N): #우선순위큐에 회의시간이 먼저 끝나는 회의를 우선순위로 넣어둠
    que.put((meetings[i][1],meetings[i]))
for i in range(N): #우선순위큐에서 빼서 먼저 끝나는 회의를 우선순위로 넣어둠
    meetings[i] = que.get()[1]

timetable = [meetings[0]]
count = 1
for i in range(1,N):
    if meetings[i][0] >= timetable[-1][1]:
        timetable.append(meetings[i])
        count += 1

print(count)