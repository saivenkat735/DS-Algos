class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
        self.top = -1  # Initialize top index to -1 (empty stack)

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow: Cannot push element, stack is full.")
            return
        self.top += 1
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Cannot pop element, stack is empty.")
            return None
        popped_item = self.stack.pop(self.top)
        self.top -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[self.top]

    def size(self):
        return self.top + 1


# Example usage:
stack = Stack(max_size=5)
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack size:", stack.size())  # Output: 3
print("Top element:", stack.peek())  # Output: 30

popped_item = stack.pop()
print("Popped item:", popped_item)  # Output: 30
print("Stack size after pop:", stack.size())  # Output: 2

print("Is stack empty?", stack.is_empty())  # Output: False

stack.push(40)
stack.push(50)
stack.push(60)  # Stack Overflow message will be displayed here as the max size is 5.
