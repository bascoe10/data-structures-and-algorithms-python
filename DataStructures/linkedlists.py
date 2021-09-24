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

    def delete(self, key):
        prev = self.__delete_search(key)
        node = prev.next
        if node is not None:
            prev.next = node.next
