n, d = map(int, input().split())
s = input()
ans = 0
s_list = list(s)
count = 0
ans = 0
for i in range(len(s_list)):
    if s_list[i] == "@":
        count += 1

ans = n - (count - d)

print(ans)
