a = list(map(int, input().split()))
b = list(map(int, input().split()))
sam_a = 0
sam_b = 0
for i in range(len(a)):
    sam_a += a[i]

for i in range(len(b)):
    sam_b += b[i]

ans = sam_a - sam_b + 1

print(ans)

