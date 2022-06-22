# .(빈칸)에 가로 세로 대각선 까지 지뢰의 개수 출력
# *(지뢰)자리는 그대로 출력
# 0 0이 입력될때까지 테스트케이스 제공

dx,dy=[-1,-1,-1,0,0,0,1,1,1],[-1,0,1,-1,0,1,-1,0,1]

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    data=[]
    for i in range(n):
        data.append(list(input()))
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]==".":
                cnt=0
                for k in range(9):
                    x = i+dx[k]
                    y = j+dy[k]
                    if x<0 or x>=n or y<0 or y>=m:
                        continue
                    if data[x][y]=="*":
                        cnt+=1
                data[i][j]=cnt
    for i in data:
        print(*i,sep='')
