class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        elif data < current.data:
            return self._search_recursive(current.left, data)
        else:
            return self._search_recursive(current.right, data)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, current, result):
        if current:
            self._inorder_traversal_recursive(current.left, result)
            result.append(current.data)
            self._inorder_traversal_recursive(current.right, result)


# Example usage:
tree = BinaryTree()
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(10)
tree.insert(25)
tree.insert(35)
tree.insert(50)

print(tree.search(25))  # Output: True
print(tree.search(45))  # Output: False

print(tree.inorder_traversal())  # Output: [10, 20, 25, 30, 35, 40, 50]
