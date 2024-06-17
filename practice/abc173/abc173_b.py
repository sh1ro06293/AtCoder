d = { "AC":0, "WA":0, "TLE":0, "RE":0}
n = int(input())

for i in range(n):
    a=input()
    d[a] += 1

print(f'AC x {d["AC"]}\nWA x {d["WA"]}\nTLE x {d["TLE"]}\nRE x {d["RE"]}')