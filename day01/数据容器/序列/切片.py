str = "万过薪月,员序程马黑来,nohtyP学" #得到黑马程序员
str1 = str[::-1]
print(str1)
list1 = str1.split(',')
print(list1[1][1::])

list2 = str.split(",")
str2 = list2[1][4::-1]
print(str2)

str3 = list2[1].replace('来', "")
print(str3[::-1])
