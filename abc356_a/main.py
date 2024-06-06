n , l , r = map(int, input().split())
a = list()
s=list()
ans = list()
for i in range(n):
    a.append(i+1)

for i in range(n):
    if l-1 <= i <= r-1:
        s.append(a[i])
        if i == r-1:
            sr = sorted(s, reverse=True)
            for j in sr:
                ans.append(j)
    else:
        ans.append(a[i])


print(*ans)


n, l, r = map(int, input().split())
a = list(range(1, n+1))
a2 = a.copy()
for i in range(l-1, r):
    a[i] = a2[r-i+l-2]

print(*a)