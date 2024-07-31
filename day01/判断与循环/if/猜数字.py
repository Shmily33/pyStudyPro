import random

num = random.randint(1, 10)
print(num)
guess = int(input("请输入您猜的数字"))
if guess == num:
    print("第一次就中")
else:
    if guess > num:
        print("大了")
    else:
        print("小了")
    guess = int(input("请输入您猜的数字"))
    if guess == num:
        print("第二次就中")
    else:
        if guess > num:
            print("大了")
        else:
            print("小了")
        guess = int(input("请输入您猜的数字"))
        if guess == num:
            print("第三次就中")
        else:
            print("机会用完，都不对" + str(num))
