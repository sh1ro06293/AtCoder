n, a = map(int, input().split())
t = list(map(int, input().split()))
ans = 0

for i in range(n):
    if ans < t[i]:
        ans += a + (t[i] - ans)
        print(ans)
    else:
        ans += a
        print(ans)