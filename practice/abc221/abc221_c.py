N = sorted(input(),reverse=True)
d = len(N)
ans = 0

for num in range(1<<d):
    l = ""
    r = ""
    ans_tmp = 0

    for shift in range(d):
        if num & (1<<shift):
            l = l + N[shift]

        else:
            r = r + N[shift]



    ans = max(ans,ans_tmp)

print(ans)