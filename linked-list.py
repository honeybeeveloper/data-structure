class Node(object):
    def __init__(self, value, next_pointer=None):
        self.value = value
        self.next = next_pointer


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Append the data into the linked list.
        :param data: data to add
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def delete(self, data):
        """
        Delete the data from the linked list.
        :param data: data to delete
        """
        prev_node = self.head
        if self.head.value == data:
            self.head = self.head.next
            del prev_node
        else:
            next_node = self.head.next
            while next_node:
                if next_node.value == data:
                    prev_node.next = next_node.next
                    del next_node
                    break
                prev_node = next_node
                next_node = next_node.next

    def __generate(self):
        """
        Generate the iterator from the linked list
        :return: iterator
        """
        iterator = self.head
        while iterator:
            yield iterator.value
            iterator = iterator.next
        return iterator

    def __str__(self):
        print_str = ''
        iterator = self.__generate()
        for i in iterator:
            print_str += f'{i} | '
        print(print_str)
