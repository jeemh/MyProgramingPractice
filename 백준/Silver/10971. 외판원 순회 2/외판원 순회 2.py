import sys

def allRoute(startCity,presentCity,value,cnt):
    global minCost
    if cnt == cityOfNum:
        if cityOfCost[presentCity][startCity]:
            value += cityOfCost[presentCity][startCity]
            if value<minCost:
                minCost = value
        return
    if value > minCost:
        return
    
    for i in range(cityOfNum):
        if gone[i] == False and cityOfCost[presentCity][i]:
            gone[i] = True
            allRoute(startCity, i, value + cityOfCost[presentCity][i], cnt + 1)
            gone[i] = False
    
cityOfNum = int(input())
cityOfCost = [list(map(int, input().split()))for _ in range(cityOfNum)]
minCost = sys.maxsize
gone = [False]*cityOfNum

for startCity in range(cityOfNum):
    gone[startCity] = True
    allRoute(startCity,startCity,0,1)
    gone[startCity] = False
    
print(minCost)