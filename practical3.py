def practical3(list1):
    data = []
    resurt = []
    for i in list1:
        if i not in data:
            resurt.append(i)
            data.append(i)

    return resurt

list1 = [6, 8, 5, 4, 6, 8, 9, 1, 4, 9, 12]
print(practical3(list1))