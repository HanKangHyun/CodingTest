# input
# 테스트케이스  T
# 포켓몬 이름
# 진화에 필요한 갯수 / 가지고있는 개수

# output
# 진화 몇번할수있는지 총 횟수
# 가장많이 진화하는 포켓몬의 이름 출력

n=int(input())
cnt=0
max_=0
for i in range(n):
    pname=input()
    k,m = map(int,input().split())
    evol=0
    while k<=m:
        m-=k
        m+=2
        evol +=1
    cnt+=evol
    if evol>max_:
        max_=evol
        max_name=pname


print(cnt)
print(max_name)

