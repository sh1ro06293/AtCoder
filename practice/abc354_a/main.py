h = int(input())
totall = 0
i = 0

while True:
    if totall > h:
        break
    totall += 2 ** i
    i += 1

print(i)
