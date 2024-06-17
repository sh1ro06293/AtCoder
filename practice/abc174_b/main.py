import math
n, d = map(int,input().split())
x = list()
for i in range(n):
    x.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    xy = math.sqrt((x[i][0] ** 2)+(x[i][1] ** 2))
    if xy <= d:
        ans+=1

print(ans)