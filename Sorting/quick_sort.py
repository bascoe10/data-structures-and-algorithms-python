def quickSort(iterable):
    def swap(i, j):
        if i == j:
            return
        temp = iterable[i]
        iterable[i] = iterable[j]
        iterable[j] = temp

    def partition(startidx, endidx):
        pivot = iterable[endidx]
        i = startidx - 1
        for j in range(startidx, endidx):
            if iterable[j] < pivot:
                i += 1
                swap(i, j)
        swap(i+1, endidx)
        return i + 1

    def quick_sort(startidx, endidx):
        if startidx < endidx:
            mididx = partition(startidx, endidx)
            quick_sort(startidx, mididx-1)
            quick_sort(startidx + 1, endidx)
    quick_sort(0, len(iterable) - 1)
    return iterable


def main():
    print(quickSort([1, 8, 7, 6, 5, 4, 9, 2, 3]))


if __name__ == '__main__':
    main()
