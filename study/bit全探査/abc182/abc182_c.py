N = input() # 整数で受け取ると楽
d = len(N)
ans=100


# num=(000...0)～(111...1)
for num in range(1<<d):
    # 桁を消して作れる数字
    N_tmp=""
    # 消した個数
    ans_tmp=0

    # shift=0~(d-1)
    for shift in range(d):
        # 1 & (numをshift右シフト)=1ならば
        if 1 & num>>shift == 1:
            # その桁を使う
            N_tmp = N_tmp+N[shift]
        
        # 1 & (numをshift右シフト)=0ならば
        else:
            # 桁を消した個数をカウント
            ans_tmp+=1
    
    # N_tmpが空なら
    # ⇔num=(000...0)の場合
    if N_tmp=="":
        # 次のnumへ
        continue

    if int(N_tmp)%3==0:
        # ansよりans_tmpが小さければ更新
        ans=min(ans,ans_tmp)
    
# 答えが更新されていなければ
if ans==100:
    # 「-1」を出力⇔3の倍数は作れない
    print(-1)
# 答えが更新されていれば
else:
    # 答えを出力
    print(ans)