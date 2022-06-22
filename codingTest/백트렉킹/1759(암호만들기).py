import sys
input= sys.stdin.readline
n,m = map(int,input().split())
data=[]
res=[]
ls = list(input().split())
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpm = ["a","e","i","o","u"]

# n = 비밀번호 자리 수
# m = 주어지는 문자개수

# ls 에 있는것들을 data에 알파벳 순으로 정렬후 저장
for i in range(len(alp)):
    for j in ls:
        if j==alp[i]:
            data.append(j)
#  data = ['a', 'c', 'i', 's', 't', 'w']


def dfs(x):
    if len(res) == n: # n 만큼 뽑은상태에서
        cnt=0
        for i in range(len(res)): # res 안에 모음이 들어있는 개수 체크
            for j in alpm:
                if res[i] == j :
                    cnt+=1
        if cnt>0 and (len(res)-cnt)>=2: # 모음이 하나이상 cnt>0 // 자음이 두개이상이라면 출력 (len(res)-cnt)>=2
            print(*res,sep='')
            return
        else:
            pass
    else:
        for i in range(x,m):
            if data[i] not in res:
                res.append(data[i])
                dfs(i)
                res.pop()

dfs(0)
