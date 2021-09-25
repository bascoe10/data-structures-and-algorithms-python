def quickSelect(iterable, position):
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

    def quick_select(startidx, endidx, ith):
        if startidx == endidx:
            return iterable[startidx]
        mididx = partition(startidx, endidx)
        k = mididx - startidx + 1
        if ith == k:
            return iterable[mididx]

        if ith < k:
            return quick_select(startidx, mididx - 1, ith)
        else:
            return quick_select(mididx + 1, endidx, ith - k)
    return quick_select(0, len(iterable)-1, position)


def main():
    print(quickSelect([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 10))


if __name__ == '__main__':
    main()
