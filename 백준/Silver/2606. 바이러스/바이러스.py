import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

dist = [None]*E
parent = [None]*(V+1)

for i in range(V+1):
    parent[i] = i

for i in range(E):
    u, v = map(int,sys.stdin.readline().split())
    dist[i] = [u,v]

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
    for _ in range(2):
        for a,b in dist:
            if find_parent(a) != find_parent(b):
                union(a,b)


kruskal()
virus = parent[1]
count = 0

for i in range(len(parent)):
    if parent[i] == virus:
        count+=1
print(count-1)


