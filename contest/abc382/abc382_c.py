n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(m):
    not_found = True
    for j in range(n):
        if a[j] <= b[i]:
            print(j + 1)
            not_found = False
            break
    if not_found:
        print(-1)

# このコードだとタイムアウトする
