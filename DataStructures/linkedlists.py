from Helpers.nodes import SingleListNode, DoubleListNode


class SinglyLinkedList:
    """
    This is an implementation of a singly linked list where insertions go to the from of the list
    """

    def __init__(self) -> None:
        self.__head = SingleListNode(None)
        self.__size = 0

    def __delete_search(self, key):
        current: SingleListNode = self.__head
        while current.next is not None and current.next.val != key:
            current = current.next
        return current

    def search(self, key) -> SingleListNode:
        current: SingleListNode = self.__head.next
        while current is not None and current.val != key:
            current = current.next
        return current

    def insert(self, key) -> None:
        node = SingleListNode(key)
        node.next = self.__head.next
        self.__head.next = node
        self.__size += 1

    def delete(self, key):
        prev = self.__delete_search(key)
        node = prev.next
        if node is not None:
            prev.next = node.next
            self.__size -= 1


class DoublyLinkedList:
    def __init__(self) -> None:
        self.__head = DoubleListNode(None)
        self.__size = 0

    def search(self, key) -> DoubleListNode:
        current = self.__head.next
        while current is not None and current.val != key:
            current = current.next
        return current

    def insert(self, key) -> None:
        node = DoubleListNode(key)
        node.next = self.__head.next
        if self.__head.next is not None:
            self.__head.next.prev = node
        node.prev = self.__head
        self.__head.next = node
        self.__size += 1

    def remove(self, key) -> None:
        node = self.search(key)
        if node is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev
        self.__size -= 1
