s= list(input())
count = list()
moji_list = list()
ans = "No"

for i in range(len(s)):
    count.append(s.count(s[i]))
    moji_list.append(s[i].islower())

for i in range(len(moji_list)):
    if moji_list[i] == True:
        for j in range(len(moji_list)):
            if moji_list[j] == False:
                for k in range(len(count)):
                    if count[k] != 1:
                        ans = "No"
                        break
                    else:
                        ans = "Yes"

print(ans)