# input
a,b = list(input().split())
# 결과 리스트
c=[]
# 자리수가 다르다면 0을 추가
if len(a)<len(b):
    d=len(b)-len(a)
    a="0"*d+a
elif len(b)<len(a):
    d = len(a) - len(b)
    b="0"*d+b
# -i 는 거꾸로 == 맨뒤자리수
# a,b 의 맨 뒤자리수 끼리 합쳐서 c에 저장
# 문자열은 -,+ 연산이 안되므로 인트로 감싸서 연산후
# 다시 문자열로 저장 ( 인트는 join이 안됨)
for i in range(1,len(a)+1):
        c.append(str(int(a[-i])+int(b[-i])))
# c 리스트를 거꾸로 뒤집음
c=c[::-1]
# join = 리스트안에 각 문자 사이에 어떤걸 넣을지 선택할수 있음
# 9,5,6 을 붙여서 출력하기 위함 956
c="".join(c)
print(c)