def transfergpa(point):
    list10 = [0, 4, 5, 5.5, 6.5, 7, 8, 8.5, 9, 11]
    list4 = [0, 1, 1.5, 2, 2.5, 3, 3.5, 3.7, 4]
    lista = ["F", "D", "D+", "C", "C+", "B", "B+", "A", "A+"]

    for i in range (len(list10)):
        if list10[i] > point:
            position = i -1
    
    print(lista[position], list4[position])

transfergpa(9)