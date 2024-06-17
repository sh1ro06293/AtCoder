n = list(map(int, input()))
ans = "Yes"

for i in range(len(n)-1):
    if  n[i+1] < n[i]:
        ans = "Yes"
    else:
        ans = "No"
        break

print(ans)