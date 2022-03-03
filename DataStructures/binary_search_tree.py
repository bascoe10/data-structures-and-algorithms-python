from Helpers.nodes import AdvanceTreeNode as Node


class BinarySearchTree:

    def __init__(self, root_val) -> None:
        self.__root = Node(root_val)

    def __transplant(self, u: Node, v: Node):
        if u.parent is None:
            self.__root == v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    # region Inorder Walk

    def __inorder_walk(self, node):
        if node is not None:
            self.__inorder_walk(node.left)
            print(node.val)
            self.__inorder_walk(node.right)

    def inorderWalk(self, node=None):
        if node is None:
            node = self.__root
        self.__inorder_walk(node)

    # endregion

    # region Search
    def __search(self, node, val):
        if node is None or node.val == val:
            return node

        if val < node.val:
            return self.__search(node.left)
        return self.__search(node.right)

    def search(self, val, node=None):
        if node is None:
            node = self.__root

        return self.__search(node, val)

    def iSearch(self, val, node=None):
        if node is None:
            node = self.__root

        while node is not None and val != node.val:
            if val < node.val:
                node = node.left
            else:
                node = node.right
        return node

    # endregion

    # region Min-Max

    def minimum(self, node=None):
        if node is None:
            node = self.__root

        while node.left is not None:
            node = node.left
        return node

    def maximum(self, node=None):
        if node is None:
            node = self.__root

        while node.right is not None:
            node = node.right
        return node
    # endregion

    # region Successor and Predecessor

    def successor(self, node):
        if node.right is not None:
            return self.minimum(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    # endregion

    # region Insert

    def insert(self, val):
        cparent = None
        current = self.__root

        while current is not None:
            cparent = current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        node = Node(val, cparent)
        if cparent is None:
            self.__root = node
        elif val < cparent.val:
            cparent.left = node
        else:
            cparent.right = node
    # endregion

    # region Delete

    def delete(self, node):
        if node.left is None:
            self.__transplant(node, node.right)
        elif node.right is None:
            self.__transplant(node, node.left)
        else:
            tmin = self.minimum(node.right)
            if tmin.parent != node:
                self.__transplant(tmin, tmin.right)
                tmin.right = node.right
                tmin.right.parent = tmin
            self.__transplant(node, tmin)
            tmin.left = node.left
            tmin.left.parent = tmin

    # endregion
