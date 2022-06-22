res=0
for i in range(10):
    a=int(input())
    res += a
    if res>=100:
        if abs(res-100)> abs(res-a-100):
            res=res-a
        break
print(res)





# data=[]
# sum=0
#
# for i in range(10):
#     N = int(input())
#     data.append(N)
#
# for i in data:
#     sum=sum+i
#
#     if sum >= 100:
#         if abs(sum-100)> abs(sum-i-100):
#             sum=sum-i
#         break
# print(sum)