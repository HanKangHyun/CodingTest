# A를 B 로 바꾸기..
# 가능한 연산은 두가지
# 2를 곱하기 / 숫자맨뒤에 1 추가
# 필요한 연산의 최솟값 +1 의 값 출력
# 불가능 할 시 -1 출력

#  A 부터 B 까지 의 최단거리를 구하기 bfs 사용.

"""
x * 2
x = int(str(x) + '1')
"""
from collections import deque

a, b = map(int, input().split())
ans = -1
q = deque()
q.append((a, 1))
while q:
    x, cnt = q.popleft()
    if x == b:
        ans = cnt
        break
    for nx in (x * 2, int(str(x) + '1')):
        if nx < 0 or nx > b:
            continue
        q.append((nx, cnt + 1))
print(ans)


