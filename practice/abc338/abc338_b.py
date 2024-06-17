from collections import defaultdict,Counter

s = list(input())
# d = defaultdict(int)


# for i in s:
#     d[i] += 1

d = Counter(s)
max_values =  max(d.values())

for i in sorted(d.keys()):
    if d[i] == max_values:
        print(i)
        break
