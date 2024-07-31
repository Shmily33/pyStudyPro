import random

num = 10000
for i in range(1, 21):
    x = random.randint(1, 11)

    if x < 5:
        print(f"员工{i},绩效：{x}小于5，不发工资")
    else:
        num -= 1000
        print(f"员工{i}发工资了，账户剩余{num}")
        if num < 1000:
            print("账户没钱了")
            break


