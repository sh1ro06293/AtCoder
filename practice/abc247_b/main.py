n = int(input())
l = list()
ans = "Yes"

for i in range(n):
    s, t = map(str, input().split())
    l.append(s)
    l.append(t)


for i in range(0,len(l),2):
    if (l.count(l[i]) >= 2) and (l[i] != l[i + 1]):
            if l.count(l[i+1]) >= 2:
                ans = "No"
                break
    
print(ans)


"""
tanaka taro
tanaka jiro
suzuki hanako
ok
4
tanaka taro
tanaka jiro
suzuki hanako
hanako tanaka
no

姓が２つ以上で名も２つ以上
"""