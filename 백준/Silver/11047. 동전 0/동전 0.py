import sys

N, K = map(int, sys.stdin.readline().split())
coin = [None]*N
for i in range(N):
    coin[i] = int(sys.stdin.readline())

coinCount = 0
for i in range(N):
    if K >= coin[N-1-i]:
        coinCount += K//coin[N-1-i]
        K %= coin[N-1-i]
print(coinCount)
