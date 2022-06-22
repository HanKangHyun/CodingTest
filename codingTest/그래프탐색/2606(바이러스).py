import sys
sys.setrecursionlimit(10000)
# 노드의 개수를 input 받는다
n = int(input())
# 선의 개수를 input 받는다
l = int(input())
# 선의 개수 만큼 for 문을 돌려서 한줄의 한쌍의 연결된 선의 데이터를 받는다.
data=[[]for _ in range(n+1)]
for i in range(l):
    # a,b를 받아서 따로 저장을 해야함
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

# 방문 체크할 리스트 생성
visited=[False]*(n+1)
# dfs 함수 만들기
# dfs 함수를 사용할때는 (data,visited,s) 가 필요함
def dfs(data,visited,s):
    # visited[s] 가 False라면:
    if visited[s]==False:
        # visited[s]를 True로 바꾸고
        visited[s]=True
        # data의 [s]번째를 하나씩 꺼내서 (i)
        for i in data[s]:
            # s 자리에 넣고 다시 dfs함수를 또 돌림
            dfs(data,visited,i)

# dfs 함수 실행 시작은 1
dfs(data,visited,1)
# visited의 1번째를 false로 바꿔줌 ( 1번 컴퓨터는 갯수에 포함 안하기 때문)
visited[1]=False
# visited리스트 안에 True의 개수를 출력 ( 바이러스에 감염된 컴퓨터의 개수 ,1번과 이어진 컴퓨터의 개수 )
print(visited.count(True))
print(visited)
