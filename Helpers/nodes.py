class SimpleTreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class AdvanceTreeNode:
    def __init__(self, val, parent=None, left=None, right=None) -> None:
        self.val = val
        self.parent: AdvanceTreeNode = parent
        self.left: AdvanceTreeNode = left
        self.right: AdvanceTreeNode = right


class SingleListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class DoubleListNode:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev
