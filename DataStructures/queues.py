from DataStructures.heaps import MinHeap, MaxHeap


class ArrayBasedQueue:
    def __init__(self) -> None:
        self.__container = []
        self.__size = 0

    def isEmpty(self) -> bool:
        return len(self.__container) == 0

    def enqueue(self, item) -> None:
        self.__container.append(item)
        self.__size += 1

    def dequeue(self) -> object:
        if self.__size > 0:
            self.__size -= 1
            return self.__container.pop(0)


class MinPriorityQueue(MinHeap):
    def __init__(self, container=...) -> None:
        super().__init__(container=container)


class MaxPriorityQueue(MaxHeap):
    def __init__(self, container=...) -> None:
        super().__init__(container=container)
