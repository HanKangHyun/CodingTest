# 1번 명령어 i 번째 전구를 x상태로 변경
# 2번 명령어 l 번째부터 r번째까지 전구상태를 변경 (0은1로 1은0으로)
# 3번 명령어 l 번째부터 r번째까지 전구를 끈다(0으로 만듬)
# 4번 명령어 l 번째부터 r번째까지 전구를 킨다(1로 만듬)

# input
# 첫째줄 전구의 개수 n , 명령어의개수 m
# 둘째줄 n개의 전구의 상태
# 셋째부터 m+2번째줄까지 정수 a,b,c
# a는 명령어번호  b,c 는 a가1일경우 = i,x  a가 2,3,4일경우 = l,r

n,m=map(int,input().split())
data = list(map(int,input().split()))
for i in range(m):
    a,b,c = map(int,input().split())
    if a==1:
        i,x=b,c
        data[b-1]=x
    if a>1:
        l, r= b,c
        if a==2:
            for j in range(l,r+1):
                if data[j-1]==0:
                    data[j-1]=1
                elif data[j-1]==1:
                    data[j-1]=0
        elif a==3:
            for j in range(l,r+1):
                data[j-1]=0
        elif a==4:
            for j in range(l,r+1):
                data[j-1]=1
for i in data:
    print(i,end=" ")