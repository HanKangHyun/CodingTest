n,m = map(int,input().split())
data=[]

def dfs():
    if len(data)==m:
        print(' '.join(map(str,data)))
        return
    for i in range(1,n+1):
        data.append(i)
        dfs()
        data.pop()

dfs()

