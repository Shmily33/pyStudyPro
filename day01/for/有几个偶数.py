# 1-100 不包含100
i = 0
for x in range(1, 100):
    if x % 2 == 0:
        i += 1
print(i)
