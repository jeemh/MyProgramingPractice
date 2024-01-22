import sys
sys.setrecursionlimit(10**6)

def postorder(arr, startIndex, endIndex):
    i = startIndex + 1
    if endIndex - startIndex == 0:
        print(arr[startIndex])
        return 
    if endIndex - startIndex == -1:
        return
    while i <= endIndex:
        if arr[startIndex] < arr[i]:
            break
        i += 1
    postorder(arr, startIndex+1, i-1)
    postorder(arr, i, endIndex)
    print(arr[startIndex])


arr = []
index = 0
while True:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break
    index += 1
postorder(arr,0,index-1)