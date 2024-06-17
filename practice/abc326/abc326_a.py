x, y = map(int, input().split())
kai = x - y
ans = "Yes"

if kai < -2:
    ans = "No"
elif 3 < kai:
    ans = "No"

print(ans)