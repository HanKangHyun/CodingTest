data=list(range(1,31))
for _ in range(28):
    a=int(input())
    data.remove(a)
data.sort()
for i in range(2):
    print(data[i])

