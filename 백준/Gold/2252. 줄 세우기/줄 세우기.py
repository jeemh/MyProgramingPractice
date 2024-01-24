import sys

graph = {}

N, M = map(int,sys.stdin.readline().split())
entryOrder = [0]*(N+1)
for i in range(1,N+1):
    graph[i] = []

for _ in range(M):
    A, B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
    entryOrder[B] += 1

def topologySort():
    queue = []
    for i in range(1,N+1):
        if entryOrder[i] == 0:
            queue.append(i)

    while queue:
        selectNode = queue.pop(0)
        print(selectNode)
        for node in graph[selectNode]:
            entryOrder[node] -= 1
            if entryOrder[node] == 0:
                queue.append(node)
        entryOrder[selectNode] = -1
        del graph[selectNode]
        
topologySort()

