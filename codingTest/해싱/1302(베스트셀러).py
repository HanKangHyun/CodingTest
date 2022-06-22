n=int(input())
data=[]
A=dict()
res=[]
for i in range(n):
    data.append(input())

for i in set(data):
    A[i]=data.count(i)

maxnum=0
for k,v in A.items():
    if v>maxnum:
        maxnum=v

for k,v in A.items():
    if v == maxnum:
        res.append(k)
res.sort()
print(res[0])