# import sys
# input=sys.stdin.readline
# n,m = map(int,input().split())  # n 걸그룹의 수 // m 문제의수
#
# Team=[[]for i in range(n)]
#
# for i in range(n):
#
#     TeamName=input().strip()
#     Team[i].append(TeamName)
#     TeamNum=int(input())
#     for j in range(TeamNum):
#         A = input().strip()
#
#         Team[i].append(A)
#
#
# for i in range(m):
#     Name=input().strip()
#     Q = int(input())
#     if Q == 1:
#         for i in range(len(Team)):
#             if Name in Team[i]:
#                 print(Team[i][0])
#     else:
#         for i in range(len(Team)):
#             if Name in Team[i]:
#                 print(*Team[i][1:],sep='\n')

import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # n 걸그룹의 수 // m 문제의수

Team = dict()

for i in range(n):
    Teamlst = []
    TeamName = input().strip()
    TeamNum = int(input())
    for j in range(TeamNum):
        A=input().strip()
        Teamlst.append(A)
    Team[TeamName]=Teamlst
Team = sorted(Team.items(), key=lambda item: item[1])
for j in range(len(Team)):
    Team[j][1].sort()

for i in range(m):
    Name=input().strip()
    Q= int(input())
    if Q == 1:
        for j in range(len(Team)):
            if Name in Team[j][1]:
                print(Team[j][0])
    else:
        for j in range(len(Team)):
            if Name in Team[j]:
                print(*Team[j][1], sep='\n')

