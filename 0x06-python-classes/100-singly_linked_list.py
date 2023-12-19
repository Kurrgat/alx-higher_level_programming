#!/usr/bin/python3

"""A class Node that defines a node of a singly linked list """


class Node:
    """"defines a node"""

    def __init__(self, data, next_node=None):
        """initializes the node with instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data attribute"""

        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (
                current.next_node is not None
                and current.next_node.data < new_node.data
            ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")
