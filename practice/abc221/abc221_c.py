N = input()
d = len(N)

for num in range(1<<d):
    # 分離した数
    kouho1_tmp = ""
    kouho2_tmp = ""
    # 積候補
    ans_tmp = ""
    for shift in range(d):
        if 