import sys

N, totalWeight = map(int,sys.stdin.readline().split())

items = [None]*(N+1)
for i in range(1,N+1):
    items[i] = list(map(int,sys.stdin.readline().split()))

DP = [[0] * (totalWeight+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,totalWeight+1):
        if j >= items[i][0]:
            DP[i][j] = max(items[i][1] + DP[i-1][j-items[i][0]], DP[i-1][j])
        else:
            DP[i][j] = DP[i-1][j]

print(DP[N][totalWeight])

# 참고 영상 : https://www.youtube.com/watch?v=8LusJS5-AGo&t=57s
