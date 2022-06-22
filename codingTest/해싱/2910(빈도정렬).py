# import sys
# from collections import defaultdict
# input=sys.stdin.readline
# A = defaultdict(int)
# B=dict()
# n,m = map(int,input().split())
# data=list(map(int,input().split()))
# for i in data:
#     A[i]+=1
# res=[]
# for i in A:
#     B[i]=A[i]
#
# for i in B:
#     res.append((str(i)+' ')*B[i])
#
# res.sort(key=len,reverse=True)
# res[-1]=str(res[-1][:-1])  ### 맨 뒤에 공백 제거 혹시몰라서
# for i in res:
#     print(i,end='')
#
# import sys
# from collections import defaultdict
# input=sys.stdin.readline
# A = defaultdict(int)
#
# n,m = map(int,input().split())
# data=list(map(int,input().split()))
# for i in data:
#     A[i]+=1
# res=[]
#
# for i in A:
#     res.append((str(i)+' ')*A[i])
#
# # res.sort(key=len,reverse=True)
# res= sorted(res)
# res[-1]=str(res[-1][:-1])  ### 맨 뒤에 공백 제거 혹시몰라서
# print(*res,sep='')
#

n,m = map(int,input().split())
A = list(map(int, input().split()))
data = dict()
res=[]
for i in A:
    data[i]=A.count(i)
# print(data)

new_data = sorted(data.items(), key=lambda x:x[1],reverse=True)
for i in range(len(new_data)):
    res.append((str(new_data[i][0])+' ')*new_data[i][1])
res[-1] = str(res[-1][:-1])  ### 맨 뒤에 공백 제거 혹시몰라서
print(*res, sep='')