n = int(input())
p = list(map(int,input().split()))
q = int(input())
for i in range(q):
    a = list(map(int,input().split()))
    for j in range(n):
        if p[j] == a[0]:
            print(a[0])
            break
        elif p[j] == a[1]:
            print(a[1])
            break