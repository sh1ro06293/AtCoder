n, d = map(int, input().split())
s = list(input())
count = 0
s_list_reversed = s[::-1]

for i in range(d):
    for j in range(len(s)):
        if s_list_reversed[j] == "@":
            s_list_reversed[j] = "."
            break

print("".join(s_list_reversed[::-1]))
