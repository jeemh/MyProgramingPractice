import sys

num = int(sys.stdin.readline())

memo = [None]*(num+1)
def pibonaci(num):
    if num == 0:
        memo[0] = 0
        return 0 
    
    if num == 1:
        memo[1] = 1
        return 1
    
    if memo[num-1] != None:
        a = memo[num-1]
    else:
        a = pibonaci(num-1)
    if memo[num-2] != None:
        b = memo[num-2]
    else:
        b = pibonaci(num-2)

    memo[num] = a+b
    return a + b

print(pibonaci(num))