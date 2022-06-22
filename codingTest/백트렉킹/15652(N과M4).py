# n,m = map(int,input().split())
# data=[]
# res=[]
# res1=[]
# def dfs():
#     if len(data)==m:
#         res.append(data[0:])
#         # print(' '.join(map(str,data)))
#         return
#     for i in range(1,n+1):
#         data.append(i)
#         dfs()
#         data.pop()
#
# dfs()
#
# # 정렬
#
# for i in range(len(res)):
#     res[i].sort()
# res = set(map(tuple, res))
# res.sort(key=lambda x:-x[0])
# for i in res:
#     print(*i)
# # # 중복제거
# # for i in res:
# #     if i not in res1:
# #         res1.append(i)
# # # 출력
# # for i in res1:
# #     print(*i)


n, m = map(int, input().split())

s = []


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)

# 4 2
# dfs(1)
# => for문은 1,n+1
# => s.append(1)  s=[1]
# #s.pop()
# dfs(1)
# => for문은 1,n+1
# => s.append(1)  s=[1,1]
# print(s) == [1,1]
# s.pop() 실행 ==> s = [1]
# 두번째 i 실행
# s.append(2) == s=[1,2]
# dfs(2)
# =>len==m: print(s) == [1,2]
# s.pop()== s =[1]
# 세번째 i 실행
# s.append(3) == s=[1,3]
# dfs(3)
# len(s)==m : print(s) == [1,3]
# pop == s=[1]
# 네번째 i 실행
# s.append(4) ==s=[1,4]
# dfs(4)
# len(s)==m => print(s) => [1,4]
# pop() == s=[1]
# 4번 for 문 끝나고
#      밀려있던 pop()실행 == s =[]
# dfs(1)에서의 for문 네바뀌가 끝나고
# 중간에 나왔다가 밀렸던 dfs(2)가 실행되고
# for 문이 2,n+1 로 돌아감
# dfs(2)
# = > s.append(2)
# s = [2]
# #pop()
# dfs(2)
# => for문은 1,n+1
# => s.append(2)  s=[2,2]
# print(s) == [2,2]
# s.pop() 실행 ==> s = [2]
# 두번째 i 실행
# s.append(3) == s=[2,3]
# dfs(3)
# =>len==m: print(s) == [2,3]
# s.pop()== s =[2]
# 세번째 i 실행
# s.append(4) == s=[2,4]
# dfs(4)
# len(s)==m : print(s) == [2,4]
# pop == s=[2]
#
# 3번 for 문 끝나고  (2,n+1)
#      밀려있던 pop()실행 == s =[]
# dfs(2)에서의 for문 세바뀌가 끝나고
# 중간에 나왔다가 밀렸던 dfs(3)가 실행되고
# for 문이 3,n+1 로 돌아감
# dfs(3)
# = > s.append(3)
# s = [3]
# # pop()
# dfs(3)
# = > s.append(3)
# s = [3, 3]
# print(s) == [3, 3]
# s.pop()
# 실행 == > s = [3]
# 두번째
# i
# 실행
# s.append(4) == s = [3, 4]
# dfs(4)
# = > len == m: print(s) == [3, 4]
# s.pop() == s = [3]
#
# 2번 for 문 끝나고  (3,n+1)
#      밀려있던 pop()실행 == s =[]
# dfs(3)에서의 for문 두바뀌가 끝나고
# 중간에 나왔다가 밀렸던 dfs(4)가 실행되고
# for 문이 4,n+1 로 돌아감
# dfs(4)
# = > s.append(4)
# s = [4]
# # pop()
# dfs(4)
# = > s.append(4)
# s = [4, 4]
# print(s) == [4, 4]
# s.pop()
# s=[4]
#
#
# for 문 한번 끝남(4,4+1)
# 밀려있던
# pop
# 실행
# s = []
#
#
