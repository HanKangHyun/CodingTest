n = int(input())
data = []

for _ in range(n):
    w, h = map(int, input().split())
    data.append((w, h))

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")