T = int(input())

memoZero = [-1]*41
memoZero[0] = 1
memoZero[1] = 0
memoOne = [-1]*41
memoOne[0] = 0
memoOne[1] = 1
memoFibo = [-1]*41
memoFibo[0] = 0
memoFibo[1] = 1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if memoFibo[n-1] == -1:
            l = fibonacci(n-1)
        else :
            l = memoFibo[n-1]
        if memoFibo[n-2] == -1:
            r = fibonacci(n-2)
        else:
            r = memoFibo[n-2]
        memoFibo[n] = l+r
        if memoZero[n-1] != -1 and memoZero[n-2] != -1:
            memoZero[n] = memoZero[n-1] + memoZero[n-2]
        if memoOne[n-1] != -1 and memoOne[n-2] != -1:
            memoOne[n] = memoOne[n-1] + memoOne[n-2]
        return memoFibo[n]
    
for _ in range(T):
    N = int(input())    
    fibonacci(N)
    print(memoZero[N],memoOne[N])