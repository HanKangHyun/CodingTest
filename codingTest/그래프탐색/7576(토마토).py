from collections import deque
import sys
a,b = map(int,input().split())
graph=[]
v=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(b):
    graph.append(list(map(int,input().split())))

def bfs(v):
    queue=deque()
    for p in range(len(v)):
        queue.append((v[p][0],v[p][1]))
    while queue:
        x,y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= b or ny < 0 or ny >= a:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                # print(graph[nx][ny])
                queue.append((nx, ny))
    result=[]
    for j in graph:
        result.append(max(j))
    for k in range(len(graph)):
        for s in graph[k]:
            if s==0:
                print(-1)
                sys.exit()

    return(max(result)-1)


# 탐색
for i in range(b):
    for j,name in enumerate(graph[i]):
        if name==1:
            v.append([i,j])


# 구현
# print(bfs(v))

print(bfs(v))