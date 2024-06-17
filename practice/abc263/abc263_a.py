a = list(map(int, input().split()))
a_list = []
for i in range(len(a)):
   a_list.append(a.count(a[i]))

if 3 in a_list and 2 in a_list:
    print("Yes")
else:
    print("No")