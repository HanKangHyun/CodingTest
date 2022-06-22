# 1을 못지나감 = 벽

# 2  출발점

# 3,4,5 중에 가까이 있는곳까지 걸리는 시간 출력

# 한칸에 1만큼 소요
import sys
from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]
n,m = map(int,input().split())
visited = [[0]*m for _ in range(n)]

graph=[]

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(a,b):
    arrive=False
    queue = deque()
    queue.append((a, b))
    visited[a][b] =1

    while queue:
        x, y = queue.popleft()
        if arrive:
            break
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if graph[nx][ny]==3 or graph[nx][ny]==4 or graph[nx][ny]==5:
                    arrive=True
                    print("TAK")
                    print(visited[nx][ny]-1)
                    sys.exit()
    if not arrive:
        print("NIE")



for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            bfs(i,j)