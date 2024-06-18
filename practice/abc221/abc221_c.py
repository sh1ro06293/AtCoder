N = sorted(input(),reverse=True)
d = len(N)
ans = 0

for num in range(1<<d):
    l = 0
    r = 0
    ans__tmp = 0

    for shift in range(d):
        print(1<<shift)
        if num & (1<<shift):
            print("num:",num) 