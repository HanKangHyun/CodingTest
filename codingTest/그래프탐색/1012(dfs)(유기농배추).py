import sys

sys.setrecursionlimit(10000000)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    if graph[x][y] == 0:
        return
    # x,y 가 1일때만 실행
    graph[x][y] = 0  # 방문처리
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        dfs(nx,ny)


n = int(input())
for i in range(n):
    # input

    M, N, K = map(int, input().split())  # M 가로 길이 , N 세로길이 , K 배추개수
    graph = [[0] * M for _ in range(N)]  # 맵 크기만큼 0으로 채움
    count = 0  # 배추 무더기 수
    for j in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
    for q in range(N):
        for w in range(M):
            if graph[q][w] == 1:
                dfs(q, w)
                count += 1
    print(count)
