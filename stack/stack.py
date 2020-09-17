"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

# class Stack:
#     def __init__(self):
#         # self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         return self.storage

#     def pop(self):
#         if self.__len__() == 0:
#             return None
#         else:
#             pop_value = self.storage[-1]
#             del self.storage[-1]
#             return pop_value


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_tail(self):
        if self.tail == None:
            return None
        else:
            return self.tail.get_value()

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length += 1

    def remove_tail(self):
        if self.head == None and self.tail == None:
            return None
        elif self.head == self.tail:
            tail_value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return tail_value
        else:
            tail_value = self.tail.get_value()
            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()
            self.tail = current_node
            self.tail.set_next(None)
            self.length -= 1
            return tail_value

    def __len__(self):
        return self.length


class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.__len__()

    def push(self, value):
        self.storage.add_to_tail(value)
        return self.storage.get_tail()

    def pop(self):
        pop_value = self.storage.get_tail()
        self.storage.remove_tail()
        return pop_value
