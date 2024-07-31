# 9*9乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        # \t制表符 在（）位置后对齐
        print(f"{j}*{i} = {i * j}\t ", end=' ')
        j += 1
    print()
    i += 1
