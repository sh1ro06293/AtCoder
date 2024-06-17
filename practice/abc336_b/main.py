n = int(input())
ctz = bin(n)[::-1].index("1")
print(ctz)
