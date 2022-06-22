j = list(map(int,input().split()))
s = list(map(int,input().split()))
j_score=[0]*len(j)
j_score[0]=j[0]

for i in range(1, len(j)):
    j_score[i]=j_score[i-1]+j[i]

s_score=[0]*len(s)
s_score[0]=s[0]

for i in range(1, len(s)):
    s_score[i]=s_score[i-1]+s[i]
res='No'

for i in range(1,9):
    if j_score[i]>s_score[i-1]:
        res='Yes'


# 1 회초에 점수를 낸다면 무조건 역전패
if j[0]>=1:
    res='Yes'

print(res)
