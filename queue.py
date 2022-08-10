class Queue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if self.queue:
            return False
        return True

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        deleted = None
        if self.is_empty():
            print('Queue is empty!')
        else:
            deleted = self.queue.pop(0)
        return deleted


class Node(object):
    def __init__(self, value, next_pointer=None):
        self.value = value
        self.next = next_pointer


class QueueLinkedList(object):
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front:
            return False
        return True

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        deleted = None
        if self.is_empty():
            print('Queue is empty!')
        else:
            deleted = self.front
            self.front = self.front.next

        # Queue is empty!
        if self.front is None:
            self.rear = None

        return deleted
