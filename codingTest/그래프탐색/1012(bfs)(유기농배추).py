from collections import deque
# input  T 테스트케이스 / 밭의가로세로 M,N / 배추의 개수 K / K줄만큼 배추의위치 좌표 a,b
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = int(input())

# bfs 함수
def bfs(a,b):
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
    return

for i in range(T):
    cnt=0
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]


    for j in range(k):
        a,b=map(int,input().split())
        graph[b][a]=1

    for a in range(n):
        for b in range(m):
            if graph[a][b]==1:
                bfs(a,b)
                cnt+=1
    print(cnt)

# # bfs로 풀어보기
# from collections import deque
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# count = 0
#
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     graph[x][y] = 0  # 방문처리
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             if graph[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 graph[nx][ny] = 0  # 방문처리
#
#
# n = int(input())
# for i in range(n):
#     # input
#
#     M, N, K = map(int, input().split())  # M 가로 길이 , N 세로길이 , K 배추개수
#     graph = [[0] * M for _ in range(N)]  # 맵 크기만큼 0으로 채움
#     count = 0  # 배추 무더기 수
#     for j in range(K):
#         a, b = map(int, input().split())
#         graph[b][a] = 1
#     for q in range(N):
#         for w in range(M):
#             if graph[q][w] == 1:
#                 bfs(q, w)
#                 count += 1
#     print(count)
#
