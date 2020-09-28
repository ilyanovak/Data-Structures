"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)
#         return self.storage[-1]

#     def dequeue(self):
#         if self.__len__() == 0:
#             return None
#         else:
#             remove_value = self.storage[0]
#             del self.storage[0]
#             return remove_value

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

    def __len__(self):
        return self.length

    def get_tail(self):
        if self.tail == None:
            return None
        else:
            return self.tail.get_value()

    def get_head(self):
        if self.head == None:
            return None
        else:
            return self.head.get_value()

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head == None and self.tail == None:
            return None
        elif self.head == self.tail:
            head_value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value
        else:
            head_value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return head_value

class Queue:
    def __init__(self):
        # self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.__len__()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        return self.storage.get_tail()

    def dequeue(self):
        if self.__len__() == 0:
            return None
        else:
            return self.storage.remove_head()
