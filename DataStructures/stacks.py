from DataStructures.linkedlists import SinglyLinkedList


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

class ListBasedStack:
    
    def __init__(self) -> None:
        self.__container = SinglyLinkedList()

    def isEmpty(self) -> bool:
        return self.__container.size() == 0

    def size(self) -> int:
        return self.__container.size()

    def peek(self) -> object:
        return self.__container.head().val

    def push(self, item) -> None:
        self.__container.insert(item)

    def pop(self) -> object:
        top = self.__container.removeHead()
        if top:
            return top.val