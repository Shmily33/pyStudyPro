# 文件的读取
f = open("D:\\Nginx\\study.txt", "r", encoding="utf-8")
print(type(f))

print(f"读取10个字节，：{f.read(10)}")
print(f"读取全部，：{f.read()}")  # 连续调用两次read,第二次read读取是在第一次的结尾开始
print("----------")
lines = f.readlines()  # 封裝到列表
print(f"读取全部行：{lines}")

for line in f:
    print(f"每一行：{line}")

f.close()

# 自动关闭close
num = 0
with open("D:\\Nginx\\study.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"每一行的数据：{line}")
        num += line.count("itheima")

print(num)
