"""
列表嵌套：有3个教室[[],[],[]]，
8名讲师['A','B','C','D','E','F','G','H']
，将8名讲师随机分配到3个教室中
"""
import random

teacher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
list = [[], [], []]
# print(len(list))
while len(teacher) > 0:
    x = random.randint(0, len(list) - 1)
    y = random.randint(0, len(teacher) - 1)
    list[x].append(teacher[y])
    teacher.remove(teacher[y])
print(list)
