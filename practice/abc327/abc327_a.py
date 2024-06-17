n = int(input())
s = list(input())
ans = "No"

for i in range(n-1):
    if (s[i] == 'a' and s[i+1] == 'b') or (s[i] == 'b' and s[i+1] == 'a'):
        ans = 'Yes'
        break 

print(ans)