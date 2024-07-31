"""
幸运数字6：输入任意数字，如数字8，生成nums列表，元素值为1~8，
从中选取幸运数字(能够被6整除)移动到新列表lucky，
打印nums与lucky。

"""
num = int(input("请输入任意数字："))
nums = list()
lucky = list()

for i in range(1, num + 1):
    nums.append(i)
    if i % 6 == 0:
        lucky.append(i)
print(nums)
print(lucky)
