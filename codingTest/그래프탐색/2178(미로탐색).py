from collections import deque
# 상 하 좌 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
#bfs
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if graph[x][y]==0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1  # 한칸 갈수록 1씩 증가시키고 마지막에 출력하기위함
                queue.append((nx, ny))

# input

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))


# 구현

for i in range(n):
    for j in range(m):
        bfs(i,j)
print(graph[n-1][m-1])
