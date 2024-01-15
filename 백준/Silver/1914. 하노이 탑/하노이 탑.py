import math
#처음지점에 있는 num번째 원판을 제외한 나머지 원판을 중간지점으로 옮긴다.
#처음지점에 있는 num번째 원판을 마지막지점으로 옮긴다.
#중간지점에 있는 원판들을 마지막지점으로 옮긴다.
def hanoi(num,start,mid,end):
    if num:
        hanoi(num-1,start,end,mid)
        print(start,end)
        hanoi(num-1,mid,start,end)
num = int(input())
print(int(math.pow(2,num))-1)
if num<=20:
    hanoi(num,1,2,3)