s = list(input())
ans = "Yes"

if  (len(set(s)) == 1) and (s[0] == "A" or s[0] == "B" or s[0] == "C"):
    pass
else:
    if s[0] == "A":
        count = 0
    elif s[0] == "B":
        count = 1
    else:
        count = 2

    for i in range(len(s)-1):
        if count == 0:
            if  s[i + 1] == "A":
                pass
            elif s[i + 1] == "B":
                count += 1
            else:
                count += 2
        elif count == 1:
            if  s[i + 1] == "B":
                pass
            elif s[i + 1] == "C":
                count += 1
            else:
                ans = "No"
        elif count == 2:
            if  s[i + 1] != "C":
                ans = "No"

        if ans == "No":
            break

print(ans)