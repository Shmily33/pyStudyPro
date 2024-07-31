money = 500000
name = None

name = input("请输入您的姓名:")


def query():
    print(f"您当前余额为{money}")


def saving():
    x = int(input("请输入要存入的金额："))
    global money
    money += x
    print(f"存入成功，账户余额{money}")

def get():
    x = int(input("请输入要取出的金额："))
    global money
    if x > money:
        print("账户余额不足")
    else:
        money -= x
        print(f"成功取出{x}元。账户余额{money}")

while True:
    print(f"{name}您好，欢迎来到黑马ATM，请选择操作：")
    print("查询余额\t 输入【1】")
    print("存款\t\t 输入【2】")
    print("取款\t\t 输入【3】")
    print("退出\t\t 输入【4】")
    num = input("请输入您的选择：")
    if num == "1":
        query()
    elif num == "2":
        saving()
    elif num == "3":
        get()
    else:
        break
