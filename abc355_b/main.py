n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort()
c = list(a + b)
c.sort()
ans = "No"

for i in range(n + m - 1):
    for j in range(n -1):
        if (c[i] == a[j]) and (c[i+1] == a[j+1]):
            ans = "Yes"
            break

print(ans)