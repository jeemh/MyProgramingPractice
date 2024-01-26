import sys
sys.setrecursionlimit(10**7)
num = int(sys.stdin.readline())

memo = [None]*(num+2)
memo[0] = 0
memo[1] = 1
    
for i in range(2,num+2):
    memo[i] = (memo[i-1] + memo[i-2])%15746

print(memo[num+1])