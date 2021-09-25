import random
import time


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


def randomizedQuickSort(iterable):
    # random.seed(int(time.time))

    def swap(i, j):
        if i == j:
            return
        temp = iterable[i]
        iterable[i] = iterable[j]
        iterable[j] = temp

    def randomized_partition(startidx, endidx):
        i = random.randint(startidx, endidx)
        swap(i, endidx)
        return partition(startidx, endidx)

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
            mididx = randomized_partition(startidx, endidx)
            quick_sort(startidx, mididx-1)
            quick_sort(startidx + 1, endidx)
    quick_sort(0, len(iterable) - 1)
    return iterable


def tailRecursiveQuickSort(iterable):

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
        while startidx < endidx:
            mididx = partition(startidx, endidx)
            quick_sort(startidx, mididx-1)
            startidx = mididx + 1
    quick_sort(0, len(iterable) - 1)
    return iterable
