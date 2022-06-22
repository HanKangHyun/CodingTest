# n,m = map(int,input().split())
# data=[]
# res=[]
# lst=[]
# def dfs():
#     if len(data)==m:
#         res.append(data[0:])
#         # print(' '.join(map(str,data)))
#         return
#     for i in range(1,n+1):
#         if i not in data:
#             data.append(i)
#             dfs()
#             data.pop()
#
# dfs()
#
# for i in range(len(res)):
#     res[i].sort()
# res.sort()
#
# # res= list(set([tuple(set(item)) for item in res]))
# # print(res)
# # res.sort()
# res1=[]
# for i in res:
#     if i not in res1:
#         res1.append((i))
# for i in res1:
#     print(*i)
#
#
#
#

n, m = map(int, input().split())

s = []


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)

# import sys
#
# input = sys.stdin.readline
# n, m = map(int, input().split()
#
# selected = []
#
#
# def dfs(k, cnt):
#     if k == n + 1:
#         if cnt == m:
#             print(*selected)
#         return
#     else:
#         selected.append(k)
#         dfs(k + 1, cnt + 1)
#         selected.pop()
#         dfs(k + 1, cnt)
#
#
# dfs(1, 0)