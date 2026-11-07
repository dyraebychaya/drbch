def quicksort(massiv):
    if len(massiv) <= 1:# 0 или 1 элемент уже отсортирован
        return massiv

    dlina = len(massiv)
    seredina_index = dlina // 2
    oporniy = massiv[seredina_index]

    levie=[]
    for x in massiv:
        if x < oporniy:
            levie.append(x)

    seredina= []
    for x in massiv:
        if x == oporniy:
            seredina.append(x)

    pravye = []
    for x in massiv:
        if x > oporniy:
            pravye.append(x)

    return quicksort(levie)+seredina+quicksort(pravye)


print(quicksort([]))
