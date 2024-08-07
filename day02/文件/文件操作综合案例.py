new_f = open("D:\\Nginx\\bill_copy.txt", "a")
with open("D:\\Nginx\\bill.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.count("测试") > 0:
            continue
        else:
            new_f.write(line)
new_f.close()
