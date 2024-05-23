s = input()
for i in range(len(s)):
    c = s.count(s[i])
    if c == 1:
        ans = s[i]
        break
    if c == len(s):
        ans = -1
        break

print(ans)