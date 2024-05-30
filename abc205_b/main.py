n = int(input())
a = list(map(int,input().split()))
ls = list()

for i in range(n):
    ls.append(i+1)

if sorted(a) == ls:
    print("Yes")
else:
    print("No")