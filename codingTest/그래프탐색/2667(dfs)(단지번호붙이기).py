n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

grp=[]
cnt=0
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    # cnt 를 함수 안에서 쓰기 위하여 global
    global cnt
    # 범위 설정 (x<0 graph기준 맨왼쪽까지, x>=n 맨오른쪽까지, y<0 맨윗줄까지,y>=n 맨아랫줄까지)
    if x<0 or x>=n or y<0 or y>=n:
        return False
    # 1을 발견하면 0으로 바꾸고 cnt+1 해준다
    # 1에서 상하좌우를 다 돌아본다
    # 전부 다 돌고 이어진 1 이 없다면 True를 리턴해준다
    if graph[x][y]==1:
        cnt+=1
        graph[x][y] = 0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True
# 구현
# 0,0 부터 6,6 까지 dfs함수를 돌린다
# True가 나오면 == 1을발견하고 근처 1을 전부 돌고 난뒤
# grp에다가 cnt를 넣어주고 cnt 초기화

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            grp.append(cnt)
            cnt=0
# 단지수 출력
print(len(grp))
# 오름차순으로
grp.sort()
# 집의 개수 출력
for i in grp:
    print(i)