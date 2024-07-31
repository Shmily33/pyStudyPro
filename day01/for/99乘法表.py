# for x in range(1, 10):
#     for y in range(1, 10):
#         if y <= x:
#             print(f"{y}*{x} = {y * x}\t",end=" ")
#     print()
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{y}*{x} = {y * x}\t", end=" ")
    print()
