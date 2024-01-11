def practical1(list1, root):
    list2 = []
    for i in range(len(list1)):
        list2.append(abs(list1[i]-root))

    min = list2[0]
    position = 0
    listPosition = []

    for i in range(len(list2)):

        if min == list2[i]:
            run = True
            listPosition.append(i)

        if list2[i] < min:
            min = list2[i]
            position = i
            listPosition = [position]
            run = False
    
    if run:
        return listPosition
    else:
        return position

list1 = [212, 34, 5, 6, 7, 21, 656, 767, 12, 33]
print(practical1(list1, 35))