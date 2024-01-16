def pibonaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    presentNum = 0
    beforeNum = 1
    doubleBeforeNum = 0
    cnt = 0
    for i in range(2,n+1):
        presentNum = beforeNum + doubleBeforeNum
        doubleBeforeNum = beforeNum
        beforeNum = presentNum
        cnt += 1
    return presentNum

print(pibonaci(int(input())))