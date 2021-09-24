def heapSort(iterable):
    # region Modified Max Heap
    size = len(iterable)
    left_child = (lambda i: (2 * i) + 1)
    right_child = (lambda i: (2 * i) + 2)

    def exchange(idx1, idx2) -> None:
        temp = iterable[idx1]
        iterable[idx1] = iterable[idx2]
        iterable[idx2] = temp

    def heaplify(idx) -> None:
        left = left_child(idx)
        right = right_child(idx)
        largest_idx = idx
        if left < size and iterable[left] > iterable[idx]:
            largest_idx = left

        if right < size and iterable[right] > iterable[largest_idx]:
            largest_idx = right

        if largest_idx != idx:
            exchange(idx, largest_idx)
            heaplify(largest_idx)

    def build_heap() -> None:
        for i in reversed(range(size // 2)):
            heaplify(i)

    if size > 1:
        build_heap()
    # endregion

    build_heap()
    for i in reversed(range(1, len(iterable))):
        exchange(0, i)
        size -= 1
        heaplify(0)
    return iterable


def main():
    print(heapSort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


if __name__ == '__main__':
    main()
