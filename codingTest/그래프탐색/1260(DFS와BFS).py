# from collections import deque
# # input 받기
# n,m,v = map(int,input().split())
# data=[[]for i in range(n+1)]
# # 방문 체크 할 리스트 생성
# visited=[False]*(n+1)
#
# for i in range(m):
#     a,b = map(int,input().split())
#     # 입력받은 데이터를 리스트에 저장
#     data[a].append(b)
#     data[b].append(a)
# # 데이터를 정렬해야 낮은순서부터 돌아감
# for i in range(1,len(data)):
#     data[i].sort()
#
# # dfs 함수 만들기
# def dfs(v):
#     # v 를 한칸띄고 옆으로 쭉 출력 == 최종 결과
#     print(v,end=' ')
#     # 방문체크하고
#     visited[v] = True
#     # 데이터의[v]= v와 연결된 노드들
#     for i in data[v]:
#         if not visited[i]: # visited[i]가 False 라면
#             dfs(i)
#
# # bfs 함수 만들기
# def bfs(v):
#     visited[v] = True
#     #deque 사용
#     queue=deque([v])
#     # queue 진행
#     while queue:
#         p = queue.popleft()
#         # v 를 한칸띄고 옆으로 쭉 출력 == 최종 결과
#         print(p,end=' ')
#         for i in data[p]:
#             # if visited[i]==False:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#
# # 출력
# dfs(v)
# # dfs 출력 후 visited 초기화
# visited=[False]*(n+1)
# # 다음 줄로 출력하기
# bfs(v)
#

