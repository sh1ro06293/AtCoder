s  = list()
for i in range(3):
    s.append(input())

t = list(map(int, input()))

for i in t:
    print(s[i-1], end="")