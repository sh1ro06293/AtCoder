## [C問題](https://atcoder.jp/contests/abc182/tasks/abc182_c)

各桁に 0 or 1 を割り当てるに割り当て、
0は消す桁
1は消さない桁
2進数で全パターン作る

ex) 135283
    101100
       152
これを全全パターン作成する


# 問題メモ

``py
for num in range(1<<d):
```
これは1をd個文左シフトしている
d=3なら
000 の 0 から
111 の 7 まで
ループすることを表している。


```py
for shift in range(d):
        # 1 & (numをshift右シフト)=1ならば
        if 1 & num>>shift == 1:
            # その桁を使う
            N_tmp = N_tmp+N[shift]
```
for shift in range(d):
これはd=3なら0から2まで右シフトしていく
1だったらその数を記入する

