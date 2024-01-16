global zeroCnt
zeroCnt = 0
global oneCnt
oneCnt = 0

def is_all_fill(arr):
    n = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != n:
                return False
    return True

def copy_arr(arr,startX,startY,endX,endY):
    returnArr = [[None] * (endY - startY + 1) for _ in range(endX - startX + 1)]
    k = 0
    for i in range(startX,endX+1):
        l = 0
        for j in range(startY,endY+1):
            returnArr[k][l] = arr[i][j]
            l += 1
        k += 1
    return returnArr

def recursion(arr):
    global zeroCnt
    global oneCnt
    if is_all_fill(arr):
        if arr[0][0] == 1:
            oneCnt += 1
        else:
            zeroCnt += 1
    else:
        copyArr = [None] * 4
        
        copyArr[0] = copy_arr(arr, 0, 0, len(arr)//2-1, len(arr)//2-1)
        copyArr[1] = copy_arr(arr, 0, len(arr)//2, len(arr)//2-1, len(arr)-1)
        copyArr[2] = copy_arr(arr, len(arr)//2, 0, len(arr)-1, len(arr)//2-1)
        copyArr[3] = copy_arr(arr, len(arr)//2, len(arr)//2, len(arr)-1, len(arr)-1)
        # copyArr[0] = arr[0:len(arr)//2, 0:len(arr)//2]
        # copyArr[1] = arr[0:len(arr)//2, len(arr)//2:len(arr)-1]
        # copyArr[2] = arr[len(arr)//2+1:len(arr)-1, 0:len(arr)//2]
        # copyArr[3] = arr[len(arr)//2+1:len(arr)-1, len(arr)//2+1:len(arr)-1]
        recursion(copyArr[0])
        recursion(copyArr[1])
        recursion(copyArr[2])
        recursion(copyArr[3])


n = int(input())
arr = [None]*n
for i in range(n):
    arr[i] = list(map(int, input().split()))

recursion(arr)
print(zeroCnt)
print(oneCnt)
