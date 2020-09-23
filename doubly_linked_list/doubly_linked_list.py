"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.next = next
        self.value = value
        self.prev = prev

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.__len__() == 0:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
        elif self.__len__() == 1:
            self.head = ListNode(value, prev=self.tail)
            self.tail.next = self.head
            self.length += 1
        else:
            new_head = ListNode(value, prev=self.head)
            self.head.next = new_head
            self.head = new_head
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.__len__() == 0:
            return None
        elif self.__len__() == 1:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value
        else:
            head_value = self.head.value
            self.head = self.head.prev
            self.head.next = None
            self.length -= 1
            return head_value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.__len__() == 0:
            self.head = ListNode(value, prev=None, next=None)
            self.tail = self.head
            self.length += 1
        elif self.__len__() == 1:
            self.tail = ListNode(value, prev=None, next=self.head)
            self.head.prev = self.tail
            self.length += 1
        else:
            new_tail = ListNode(value, prev=None, next=self.tail)
            self.tail.prev = new_tail
            self.tail = new_tail
            self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.__len__() == 0:
            return None
        elif self.__len__() == 1:
            remove_value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return remove_value
        else:
            remove_value = self.tail.value
            self.tail = self.tail.next
            self.tail.prev = None
            self.length -= 1
            return remove_value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.delete(node) != None:
            node_value = node.value
            self.add_to_head(node_value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.delete(node) != None:
            node_value = node.value
            self.add_to_tail(node_value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        if node == None:
            return None
        if self.__len__() == 0:
            return None
        elif self.__len__() == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            curr_node = self.tail
            while curr_node != None:
                if curr_node.value == node.value and curr_node is self.tail:
                    self.tail = self.tail.next
                    self.tail.prev = None
                    self.length -= 1
                    return f'Node is deleted'
                elif curr_node.value == node.value and curr_node is self.head:
                    self.head = self.head.prev
                    self.head.next = None
                    self.length -= 1
                    return f'Node is deleted'
                elif curr_node.value == node.value:
                    curr_node.next.prev = curr_node.prev
                    curr_node.prev.next = curr_node.next
                    self.length -= 1
                    return f'Node is deleted'
                curr_node = curr_node.next

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        if self.__len__() == 0:
            return None
        else:
            values_list = []
            curr_node = self.tail
            while curr_node is not None:
                values_list.append(curr_node.value)
                curr_node = curr_node.next
            return max(values_list)
