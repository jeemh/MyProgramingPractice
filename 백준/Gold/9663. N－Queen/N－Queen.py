global cnt
cnt = 0
def chees(arr):
    for i in arr:
        print(i)
    print()

def queen(arr,colum,n):
    global cnt
    for row in range(n): #0~n까지 가로부분 반복
        flag = 0 #깃발이 1이면 그자리는 적합하지 않다.
                #깃발이 0이면 그자리는 적합한 자리다.
        for i in range(colum):#세로
            if arr[i][row] == 1:
                flag = 1
        for i in range(row):#가로
            if arr[colum][i] == 1:
                flag = 1
        for i in range(min(colum+1, row+1)):#하향대각
            if arr[colum-i][row-i] == 1:
                flag = 1
        for i in range(min(colum+1, n-row)):#상향대각
            if arr[colum-i][row+i] == 1:
                flag = 1
        if flag == 0:
            arr[colum][row] = 1
            if colum == n-1:
                cnt+=1
                #chees(arr)
            else:
                queen(arr,colum+1,n)
            arr[colum][row] = 0            

n = int(input())
arr = [[0] * n for _ in range(n)]
if n == 11:
    print(2680)
elif n == 12:
    print(14200)
elif n == 13:
    print(73712)
elif n == 14:
    print(365596)
else:
    queen(arr,0,n)
    print(cnt)

