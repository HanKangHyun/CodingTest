# n,m=map(int,input().split())
# nolisten=[]
# nosee=[]
# res=[]
# for i in range(n):
#     nolisten.append(input())
#
# for i in range(m):
#     nosee.append(input())
# for i in nolisten:
#     for j in nosee:
#         if i==j:
#             res.append(j)
# res.sort()
# print(len(res))
# for i in res:
#     print(i)
#
#
# n,m=map(int,input().split())
# data=[]
#
# res=[]
# for i in range(n):
#     data.append(input())
#
# for i in range(m):
#     a=input()
#     if a in data:
#         res.append(a)
#
# res.sort()
# print(len(res))
# for i in res:
#     print(i)


n,m=map(int,input().split())
data=dict()
res=[]
for i in range(n):
    data[input()]=False
for i in range(m):
    A=input()
    if A in data:
        data.pop(A) ####
        res.append(A)
print(len(res))
res.sort()
for i in res:
    print(i)