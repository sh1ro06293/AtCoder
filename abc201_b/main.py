# n = int(input())
# d = dict()

# for i in range(n):
#     s, t = map(str, input().split())
#     d[s] = int(t)
# ds = list(d.keys())
# dv = list(d.values())
# dv.sort(reverse=True)

# for i in range(n):
#     if d[ds[i]] == dv[1]:
#         print(ds[i])


n = int(input())

dic = {}
for i in range(n):
    s, t = input().split()
    dic[int(t)] = s
target = sorted(dic.keys(), reverse=True)[1]
print(dic[target])