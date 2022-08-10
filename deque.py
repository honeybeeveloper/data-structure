class Deque(object):
    def __init__(self):
        self.deque = []

    def is_empty(self):
        if self.deque:
            return False
        return True

    def add_rear(self, data):
        self.deque.append(data)

    def add_front(self, data):
        self.deque.insert(0, data)

    def remove_rear(self):
        deleted = None
        if self.is_empty():
            print('Deque is empty!')
        else:
            deleted = self.deque.pop()
        return deleted

    def remove_front(self):
        deleted = None
        if self.is_empty():
            print('Deque is empty!')
        else:
            deleted = self.deque.pop(0)
        return deleted
