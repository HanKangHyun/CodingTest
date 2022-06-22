import sys
input= sys.stdin.readline
n,m = map(int,input().split())
ls = list(map(int,input().split()))
ans=0
def dfs(x,val):
    global ans
    if x==n:
        if val==m:
            ans+=1
    else:
        dfs(x+1,val+ls[x])
        dfs(x+1,val)
dfs(0,0)
if m==0:
    ans-=1
print(ans)
