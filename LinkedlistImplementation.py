class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"Item {data} not found in the list.")

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.prepend(5)
linked_list.append(30)
linked_list.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

linked_list.delete(20)
linked_list.display()  # Output: 5 -> 10 -> 30 -> None

print(linked_list.search(10))  # Output: True
print(linked_list.search(20))  # Output: False
