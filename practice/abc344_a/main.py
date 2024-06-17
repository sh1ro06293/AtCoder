s = list(input())
flag = False
ans = ""

for i in range(len(s)):
    if flag:
        if s[i] == "|":
            flag = False
    else:
        if s[i] == "|":
            flag = True
        else:
            ans += s[i]
        
print(ans)