s = list(input())
t = list(input())
ans = "Yes"

if (s[len(s)-2] == t[len(t)-2]) and (s[len(s)-1] != t[len(t)-1]):
    ans = "No"
else:
    for i in range(len(s)-1):
        if s[i] != t[i]:
            si = s[i]
            s[i] = s[i+1]
            s[i+1] = si
            for j in range(len(s)-1):
                if s[j] != t[j]:
                    ans = "No"
                    break

print(ans)