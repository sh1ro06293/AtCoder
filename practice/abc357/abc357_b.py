x = input()
s = list(x)
o= 0

for i in range(len(s)):
    if s[i].isupper():
        o += 1

if o <= len(s)-o:
    # 小文字の時
    print(x.lower())
else:
    print(x.upper())