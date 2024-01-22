import sys
V,E = map(int,sys.stdin.readline().split())

dist = [[9999999 for _ in range(3)] for _ in range(E)]
parent = [None]*(V+1)

for i in range(V+1):
    parent[i] = i

for i in range(E):
    A, B, C = map(int,sys.stdin.readline().split())
    dist[i] = [C,A,B]

dist.sort()

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(a,b):
    ap = find_parent(a)
    bp = find_parent(b)

    if ap == bp:
        return
    if ap > bp:
        parent[ap] = bp
    else :
        parent[bp] = ap

def kruskal():
    sum = 0
    for c,a,b in dist:
        if find_parent(a) != find_parent(b):
            sum += c
            union(a,b)
        
        # if parent[dist[i][1]] > min(parent[dist[i][1]],parent[dist[i][2]]):
        #     parent[dist[i][1]] = min(parent[dist[i][1]],parent[dist[i][2]])

        # if parent[dist[i][2]] > min(parent[dist[i][1]],parent[dist[i][2]]):
        #     parent[dist[i][2]] = min(parent[dist[i][1]],parent[dist[i][2]])
   
    return sum
        
print(kruskal())

