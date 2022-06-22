# 문장에 알파벳의 모든글자가 포함되어있으면 Y 그렇지않으면 N 출력
# 모든 알파벳은 소문자로 주어지고 마지막에 * 로 종료

#

while True:
    alp = list(range(97,123))
    a = list(input())
    if "*" in a:
        break
    for i in a:
        if ord(i) in alp:
            alp.remove(ord(i))
    if len(alp)>0:
        print("N")
    else:
        print("Y")

#
# from string import ascii_lowercase
# while True:
#     alp = list(ascii_lowercase)
#     A = list(input())
#     if '*' in A:
#         break
#     A=list(set(A))
#
#     for i in A:
#         if i in alp:
#             alp.remove(i)
#     if len(alp) == 0 :
#         print('Y')
#     else:
#         print('N')
