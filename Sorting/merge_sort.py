import math


def mergeSort(iterable):
    def merge(startidx, mididx, endidx):
        num_items_in_left_container = mididx - startidx + 1
        num_items_in_right_container = endidx - mididx
        left_container = [0] * (num_items_in_left_container + 1)
        right_container = [0] * (num_items_in_right_container + 1)
        left_container[-1] = math.inf
        right_container[-1] = math.inf

        for i in range(num_items_in_left_container):
            left_container[i] = iterable[startidx + i]

        for j in range(num_items_in_right_container):
            right_container[j] = iterable[mididx + j + 1]

        i = j = 0
        for k in range(startidx, endidx+1):
            if left_container[i] <= right_container[j]:
                iterable[k] = left_container[i]
                i += 1
            else:
                iterable[k] = right_container[j]
                j += 1

    def merge_sort(startidx, endidx):
        if startidx < endidx:
            mididx = (startidx + endidx) // 2
            merge_sort(startidx, mididx)
            merge_sort(mididx+1, endidx)
            merge(startidx, mididx, endidx)
    merge_sort(0, len(iterable)-1)
    return iterable
