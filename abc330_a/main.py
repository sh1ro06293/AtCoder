n, l = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in range(n):
    if l <= a[i]:
        count += 1

print(count)
