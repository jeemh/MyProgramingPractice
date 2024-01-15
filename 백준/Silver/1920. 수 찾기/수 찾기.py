def binarySearch(a,b):

    startIndex = 0
    midIndex = (len(a)-1)//2
    lastIndex = len(a)-1
    while(True):
        if startIndex > lastIndex:
            return False
        if a[midIndex] == b:
            return True
        elif a[midIndex] < b:
            startIndex = midIndex + 1
        elif a[midIndex] > b:
            lastIndex = midIndex - 1
        midIndex = (startIndex + lastIndex) // 2

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in b:
    if binarySearch(a,i):
        print(1)
    else:
        print(0)
    