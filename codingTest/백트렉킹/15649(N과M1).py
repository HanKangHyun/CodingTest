n,m = map(int,input().split())
data=[]

def dfs():
    if len(data)==m:
        print(' '.join(map(str,data)))
        return
    for i in range(1,n+1):
        if i not in data:
            data.append(i)
            dfs()
            data.pop()

dfs()


# 방문체크
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# data=[]
# visited=[False]*n
#
# def dfs():
#
#     if len(data)==m:
#         print(*data)
#         return
#     for i in range(1,n+1):
#         if not visited[i-1]:
#             data.append(i)
#             visited[i-1]=True
#             dfs()
#             visited[i-1]=False
#             data.pop()
# dfs()
