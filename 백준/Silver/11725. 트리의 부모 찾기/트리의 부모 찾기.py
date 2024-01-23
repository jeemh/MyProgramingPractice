import sys

N = int(sys.stdin.readline())
tree = [None]*(N-1)
graph = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int,sys.stdin.readline().split())
    # tree[i] = [a, b]
    graph[a].append(b)
    graph[b].append(a)

ans = [0]*(N+1)

def bfs():
    queue = []
    queue.append(1)

    while queue:
        now = queue.pop(0)
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
res = ans[2:]
for x in res:
    print(x)
# parentsToBaby = []
# queue = []
# check = []
# cnt = 0

# queue.append(1)

# while queue:
#     parent = queue.pop(0)
#     check.append(parent)

#     for a, b in tree[:]:
#         if a == parent :
#             queue.append(b)
#             parentsToBaby.append([b,parent])
#             tree.remove([a,b])
             
#         if b == parent :
#             queue.append(a)
#             parentsToBaby.append([a,parent])
#             tree.remove([a,b])
            
#     #     cnt += 1
#     # if len(queue)+len(check) == N:
#     #     break
#     #     #print("<tree: ",tree,">")
        
    
# # print(tree)
# #print(cnt)
# parentsToBaby.sort()
# for a, b in parentsToBaby:
#     print(b)

