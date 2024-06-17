n, m = map(int, input().split())
h = list(map(int, input().split()))
i = 0
while (i < n) and (h[i] <= m):
    m -= h[i]
    i+=1

print(i)