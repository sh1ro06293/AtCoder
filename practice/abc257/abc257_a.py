n, x = map(int, input().split())
ans = []
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(len(abc)):
    for j in range(n):
        ans.append(abc[i])

print(ans[x-1])