N = int(input())
data = [[] for i in range(11)]
cnt = 0
# 소는 1<= a <=10
for _ in range(N):
    a, b = map(int, input().split())
    data[a].append(b)


# for 문 돌려서 a 가 같을 때 b 가 같다면 pass 다르면 cnt=+1

for i in range(len(data)):
    res = []
    for j in data[i]:
        if len(res)>0:
            if res[0] == j :
                continue
            elif res[0] != j :
                cnt+=1
                res[0]=j
        else:
            res.append(j)
print(cnt)
