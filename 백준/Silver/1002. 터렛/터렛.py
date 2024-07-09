import math

T = int(input())

for i in range(T): 
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if dist == 0 and r1 == r2:
        print(-1)  # 두 원이 동일할 때
    elif dist == abs(r1 - r2) or dist == (r1 + r2):
        print(1)  # 두 원이 내접하거나 외접할 때
    elif abs(r1 - r2) < dist < (r1 + r2):
        print(2)  # 두 원이 두 점에서 만날 때
    else:
        print(0)  # 두 원이 만나지 않을 때
