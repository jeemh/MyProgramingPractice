import sys

graph = {}

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

entryOrder = [0]*(N+1)

for i in range(1,N+1):
    graph[i] = []

for _ in range(M):
    A, B, C = map(int,sys.stdin.readline().split())
    graph[B].append([A,C])
    entryOrder[A] += 1

eachCost = [[0 for _ in range(N+1)] for _ in range(N+1)]

def topologySort():
    queue = []
    for i in range(1,N+1):
        if entryOrder[i] == 0:
            queue.append(i)
        
    while queue:
        selectNode = queue.pop(0)

        for goods,cost in graph[selectNode]:

            if eachCost[selectNode].count(0) == N+1: #기본부품이면
                eachCost[goods][selectNode] += cost
            else: #기본부품이 아니면
                for i in range(1,N+1): 
                    eachCost[goods][i] += eachCost[selectNode][i] * cost

            entryOrder[goods] -= 1
            if entryOrder[goods] == 0: #진입차수가 0이면 큐에 해당제품을 넣음
                queue.append(goods)

        entryOrder[selectNode] = -1 #진입 후에 모든 절차가 끝나면 진입차수를 -1로 만들어주고 삭제
        del graph[selectNode]

topologySort()
cnt=0
for i in eachCost[N]:

    if i > 0:
        print(cnt,i)
    cnt += 1
