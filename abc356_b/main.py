n ,m = map(int, input().split())
a = list(map(int, input().split()))
s = list()
eiyou = list()
for i in range(m):
    eiyou.append(0)
ans = 'Yes'

for i in range(n):
    s.append(list(map(int,input().split())))

for i in range(m):
    for j in range(n):
        eiyou[i] += s[j][i]

for i in range(m):
    if a[i] > eiyou[i]:
        ans = "No"
        break

print(ans)