s = list(map(int, input()))

# ans = (s[0]+s[1]+s[2])*100 + (s[0]+s[1]+s[2])*10 + (s[0]+s[1]+s[2])
ans = sum(s) * 111

print(ans)

