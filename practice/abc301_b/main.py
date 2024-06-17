n = int(input())
a = list(map(int, input().split()))
ans = list()

for i in range(n - 1):
    ans.append(a[i])
    if a[i + 1] - a[i] >= 1:
        for j in range((a[i + 1] - a[i]) - 1 ):
            ans.append(a[i] + j + 1)
    elif a[i] - a[i + 1] >= 1:
        for j in range((a[i] - a[i + 1]) - 1):
            ans.append(a[i] - (j + 1))

ans.append(a[n-1])

print(*ans)