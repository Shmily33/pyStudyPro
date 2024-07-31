list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for i in list1:
    if i % 2 == 0:
        list2.append(i)
print(list2)
j = 0
list3 = []
while j < len(list1):
    if list1[j] % 2 == 0:
        list3.append(list1[j])
    j += 1
print(list3)
