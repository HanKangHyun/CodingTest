n, m = map(int, input().split())
data=[]
s = list(map(int,input().split()))
s.sort()

def dfs(start):
    if len(data) == m:
        print(' '.join(map(str, data)))
        return

    for i in s:
        if i not in data:
            data.append(i)
            dfs(i)
            data.pop()

dfs(1)