class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return False
        return True

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        deleted = None
        if self.is_empty():
            print('Stack is empty!')
        else:
            deleted = self.stack.pop()
        return deleted


class Node(object):
    def __init__(self, value, next_pointer=None):
        self.value = value
        self.next = next_pointer


class StackLinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        return True

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        deleted = None
        if self.is_empty():
            print('Stack is empty!')
        else:
            deleted = self.head.value
            self.head = self.head.next
        return deleted
