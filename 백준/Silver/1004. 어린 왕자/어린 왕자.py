T = int(input())

for _ in range(T):
    x1,y1,x2,y2 = map(int, input().split())
    numOfPlanet = int(input())
    through = 0
    for _ in range(numOfPlanet):
        c1,c2,r = map(int, input().split()) 
        if (x1-c1) ** 2 + (y1-c2) ** 2 < r ** 2 or (x2-c1) ** 2 + (y2-c2) ** 2 < r ** 2:
            if not ((x1-c1) ** 2 + (y1-c2) ** 2 < r ** 2 and (x2-c1) ** 2 + (y2-c2) ** 2 < r ** 2):
                through += 1
    print(through)