class MinHeap:
    def __init__(self, container=[]) -> None:
        self.__container = container
        self.__size = len(self.__container)
        self.__left = (lambda i: (2 * i) + 1)
        self.__right = (lambda i: (2 * i) + 2)
        self.__parent = (lambda i: (i // 2))
        if self.__size > 2:
            self.__build_heap()

    def __exchange(self, idx1, idx2) -> None:
        temp = self.__container[idx1]
        self.__container[idx1] = self.__container[idx2]
        self.__container[idx2] = temp

    def __increase_key(self, idx) -> None:
        while idx > 0 and self.__container[self.__parent(idx)] > self.__container[idx]:
            self.__exchange(self.__parent(idx), idx)
            idx = self.__parent(idx)

    def __heaplify(self, idx) -> None:
        left = self.__left(idx)
        right = self.__right(idx)
        smallest_idx = idx
        if left < self.__size and self.__container[left] < self.__container[idx]:
            smallest_idx = left

        if right < self.__size and self.__container[right] < self.__container[smallest_idx]:
            smallest_idx = right

        if smallest_idx != idx:
            self.__exchange(idx, smallest_idx)
            self.__heaplify(smallest_idx)

    def __build_heap(self) -> None:
        for i in reversed(range(self.__size // 2)):
            self.__heaplify(i)

    def minimum(self) -> object:
        if self.__size > 0:
            return self.__container[0]

    def extractMin(self) -> object:
        if self.__size < 1:
            return
        top = self.__container[0]
        self.__container[0] = self.__container[-1]
        self.__container.pop()
        self.__size -= 1
        self.__heaplify(0)
        return top

    def insert(self, key) -> None:
        self.__container.append(key)
        self.__size += 1
        self.__increase_key(self.__size - 1)
