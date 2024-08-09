class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


for i in range(1, 11):
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    address = input("请输入学生地址：")
    stu = student(name, age, address)
    print(f"学生{i}信息录入完成,信息为：【学生姓名；{stu.name},年龄：{stu.age},地址：{stu.address}】")
