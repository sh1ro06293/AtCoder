k = list(map(int, input().split()))
ans_list = list(range(1, 4))
ans = -1

if k[0]  != k[1]:
    ans_list.remove(k[0])
    ans_list.remove(k[1])
    ans = ans_list[0]
print(ans)
