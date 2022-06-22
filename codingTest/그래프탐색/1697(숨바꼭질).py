# input 받기

# n 이 m 까지 이동하는데 걸리는 가장빠른시간 출력

# n은 +1 -1 n*2 로 이동 가능

# n 을 시작 노드로 갈수있는길이 3가지 있다고 볼수 있음 n+1 / n-1 / n*2

# 세가지로 쭉쭉 뻗어나가서 m까지 가는 최단거리를 찾으면 됨  = bfs사용

# d라는 리스트에 범위(십만)만큼 0 을 채워 주고
# 한 층 이동하면 d 에 +1 해주는 방식으로 쭉쭉 지나가고
# x==m 이된다면 d[x]를 출력해주고 break로 끝냄
# cnt를 사용안하고 새로운 리스트 d 에 0 을 채워두고 한층갈때마다 +1을 해주는방식으로 한뒤 d를 출력함

from collections import deque


n,m = map(int,input().split())
MAX=100000
d=[0]*(MAX+1)
def bfs():
    queue=deque()
    queue.append(n)
    while queue:
        x=queue.popleft()
        if x==m:
            print(d[x])
            break
        for i in (x-1,x+1,x*2):
            if 0<= i <= MAX and not d[i]:  # i가 0<i<100000 범위안에있고, d[i]==0 이라면
                d[i]=d[x]+1
                queue.append(i)

bfs()