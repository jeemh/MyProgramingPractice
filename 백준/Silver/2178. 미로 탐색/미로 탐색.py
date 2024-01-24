import sys

N, M = map(int,sys.stdin.readline().split())
arr = [None]*N
for i in range(N):
    arr[i] = sys.stdin.readline()
maze = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        maze[i][j] = int(arr[i][j])

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def mazeSearch(x,y):
    
    queue = []
    queue.append([x,y])
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1  
mazeSearch(0,0)
print(maze[N-1][M-1])