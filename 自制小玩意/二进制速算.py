# 二进制速算游戏

import random


n = 0
istrue = 0
isfalse = 0
while True:
    
    # 随机给出一个十进制数 范围是 0-15
    x = random.randint(0,15)

    # 输入二进制数

    y = input(f"请输入{x}的二进制数（q to quit)：")

    if 'q' == y.casefold():
        print("游戏结束")
        print(f"共答{n}道题")
        print(f"你答对了{istrue}道")
        break

    y = int(y,2)
    n += 1
    if x == y:
        print("答对了")
        istrue += 1
    else:
        print("答错了")
        isfalse += 1
