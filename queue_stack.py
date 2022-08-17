class Stack:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top:
            new_node = self.StackNode(data)
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = self.StackNode(data)
        return self

    def pop(self):
        if not self.top:
            return None
        
        pop_data = self.top.data
        self.top = self.top.next
        return pop_data

class Queue:
    def __init__(self):
        self.hold_stack = Stack()
        self.flip_stack = Stack()
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, data):
        self.hold_stack.push(data)
        self._size += 1
        return self

    def dequeue(self):
        if self._size == 0:
            return None

        for i in range(1, self._size):
            self.flip_stack.push(self.hold_stack.pop())
        dequeue_data = self.hold_stack.pop()
        for i in range(1, self._size):
            self.hold_stack.push(self.flip_stack.pop())
        self._size -= 1

        return dequeue_data