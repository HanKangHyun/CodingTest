import sys
input=sys.stdin.readline

ans=list(map(int,input().split()))
selected = [0] * 10 # 내 답안지
total=0

def dfs(x):
    global total
    if x==10: # dfs(10)이라면 => 뽑은 수가 열개라면
        cnt=0 # 맞은 개수 체크하기 위하여 설정 밑에 for 문 열번 다 돌면 초기화
        for i in range(10):
            if selected[i] == ans[i]: # 정답지의[i] 번째가 내 정답의[i] 번째와 같다면 => 정답 채점
                cnt+=1 # 맞은 개수
        if  cnt >= 5:# 체점이 끝나고 5 개 이상 맞았다면
            total+=1 # 5점이상인 경우의수
    else: # 열개 뽑기 전이라면
        for i in range(1,6): # 5지선다이니까 1 부터 5번까지 모든 경우의 수를 보기 위함.
            if x>=2 and i==selected[x-1] and i == selected[x-2]:
                continue # 전전 숫자와 전숫자와 같다면 패스
            selected[x]=i
            dfs(x+1)
            selected[x]=0 # pop과 같은 역할
dfs(0)
print(total)