def heapSort(iterable):
    # region Modified Max Heap
    class MaxHeap:
        def __init__(self) -> None:
            self.size = len(iterable)
            self.left = (lambda i: (2 * i) + 1)
            self.right = (lambda i: (2 * i) + 2)
            self.parent = (lambda i: (i // 2))
            if self.size > 1:
                self.build_heap()

        def exchange(self, idx1, idx2) -> None:
            temp = iterable[idx1]
            iterable[idx1] = iterable[idx2]
            iterable[idx2] = temp

        def heaplify(self, idx) -> None:
            left = self.left(idx)
            right = self.right(idx)
            largest_idx = idx
            if left < self.size and iterable[left] > iterable[idx]:
                largest_idx = left

            if right < self.size and iterable[right] > iterable[largest_idx]:
                largest_idx = right

            if largest_idx != idx:
                self.exchange(idx, largest_idx)
                self.heaplify(largest_idx)

        def build_heap(self) -> None:
            for i in reversed(range(self.size // 2)):
                self.heaplify(i)
    # endregion

    heap = MaxHeap()
    for i in reversed(range(1, len(iterable))):
        heap.exchange(0, i)
        heap.size -= 1
        heap.heaplify(0)
    return iterable
