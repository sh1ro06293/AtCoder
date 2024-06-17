k = int(input())
a, b = list(map(str, input().split()))
a = list(a)
b = list(b)
a_10, b_10 = 0, 0
for i in range(len(a)):
    a_10 += int(a[i])*(k**(len(a)-1-i))
for i in range(len(b)):
    b_10 += int(b[i])*(k**(len(b)-1-i))

print(a_10*b_10)