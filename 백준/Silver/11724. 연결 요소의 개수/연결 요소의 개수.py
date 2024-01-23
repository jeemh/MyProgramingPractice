import sys
from collections import Counter

V,E = map(int,sys.stdin.readline().split())

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
        # parent[bp] = bp
    else :
        # parent[ap] = ap
        parent[bp] = ap

def kruskal():
    for _ in range(2):
        for a,b in dist:
            if find_parent(a) != find_parent(b):
                union(a,b)

#print(parent)
kruskal()
#print(parent)
print(len(set(parent))-1)
#elementNum = len({key: value for key, value in Counter(parent).items() if value != 1})
#print(elementNum)

