n=int(input())
A=dict()
res=[]
for i in range(n):
    a,b = input().split()
    A[a]=b
for k,v in A.items():
    if v=="enter":
        res.append(k)
res.sort(reverse=True)
print(*res,sep='\n')