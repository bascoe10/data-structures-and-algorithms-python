class ArrayBasedStack:
    def __init__(self) -> None:
        self.__container = []

    def isEmpty(self) -> bool:
        return len(self.__container) == 0

    def push(self, item) -> None:
        self.__container.append(item)

    def pop(self) -> object:
        if len(self.__container) > 0:
            return self.__container.pop()
