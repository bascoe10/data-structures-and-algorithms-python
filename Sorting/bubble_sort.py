def bubbleSort(iterable):
    num_items = len(iterable)
    for i in range(num_items - 1):
        for j in reversed(range(i, num_items)):
            if iterable[j] < iterable[j - 1]:
                temp = iterable[j]
                iterable[j] = iterable[j - 1]
                iterable[j - 1] = temp
    return iterable
