import sys
input=sys.stdin.readline

n, m = map(int, input().split())

s = sorted(map(int,input().split()))  # sorted => 정렬된 list 형식으로 변환  (즉 list함수를 포함하고있음)

res=[]
picked = [False]*(n+1)  # 방문체크
def dfs(x):
    if x==m:
        print(*res)
        return
    else:
        remember = 0 # 뽑은 숫자를 저장해놓기위한 변수
        for i in range(n):
            if picked[i] or s[i]==remember: # 뽑은적이 있거나 바로직전과 같은 수를 뽑았다면
                continue
            res.append(s[i])
            remember=s[i]
            picked[i] = True # 방문체크
            dfs(x+1) # 재귀함수
            res.pop() # 모든 경우의수 체크를 위해
            picked[i] = False # 한바퀴가 끝나면 다시 리셋
dfs(0)