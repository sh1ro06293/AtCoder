mas = list()
s = list()

for i in range(10):
    mas.append(list(map(str, input())))

for i in range(10):
    for j in range(10):
        if mas[i][j] == "#":
            s.append([i+1,j+1])            

print(f"{s[0][0]} {s[-1][0]}")
print(f"{s[0][1]} {s[-1][1]}")