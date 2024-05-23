s = list(input())
# for i in range(len(s)-1):
#     if s[i] != s[i + 1]:
#         if s[i] != s[i + 2]:
#             ans = i + 1
#             break
#         elif s[i + 1] != s[i + 2]:
#             ans = i + 2
#             break
#     else:
#         if s[i] != s[i + 2]:
#             ans = i + 3
#             break

# print(ans)

for i in range(len(s)):
    c =  s.count(s[i])
    if  c == 1:
        ans = i + 1
        break

print(ans)