# data[0] = 집의위치
# data[1]~ data[n+1] 편의점 위치
# data[-1] 페스티벌위치

# c = x+y
# d = (data[i][0])+(data[i][1])
# if d-c <= 1000: 다음 편의점으로 이동
# else print("sad")

from collections import deque
T = int(input())

def bfs():
    queue = deque()
    queue.append((data[0][0],data[0][1]))
    while queue:
        x,y=queue.popleft()
        if abs(x - data[-1][0]) + abs(y-data[-1][1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx,ny = data[i+1][0],data[i+1][1]

                if abs(x-nx)+abs(y-ny)<=1000:
                    queue.append((nx,ny))
                    visited[i]=True
    print("sad")
    return

for _ in range(T):
    n = int(input()) # 편의점 개수
    data = []
    for _ in range(n+2):
        x, y = map(int,input().split())
        data.append((x,y))
    visited=[False]*(n+1)
    bfs()







