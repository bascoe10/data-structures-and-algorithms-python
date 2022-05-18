class ArrayBasedStack:
    def __init__(self) -> None:
        self.__container = []
        self.__length = 0

    def isEmpty(self) -> bool:
        return self.__length == 0

    def size(self) -> int:
        return self.__length

    def peek(self) -> object:
        if self.__length > 0:
            return self.__container[0]

    def push(self, item) -> None:
        self.__container.append(item)
        self.__length += 1

    def pop(self) -> object:
        if self.__length > 0:
            self.__length -= 1
            return self.__container.pop()
