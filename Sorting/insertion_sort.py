def insertionSort(iterable):
    for j in range(1, len(iterable)):
        key = iterable[j]
        i = j - 1
        while i >= 0 and iterable[i] > key:
            iterable[i+1] = iterable[i]
            i -= 1
        iterable[i + 1] = key
    return iterable
