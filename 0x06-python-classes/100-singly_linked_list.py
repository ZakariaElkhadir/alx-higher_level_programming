#!/usr/bin/python3
"""node class object"""


class Node:


    def __init__(self ,data ,next_node=None):

       self.data = data
       self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
    """initialize two object"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        selInitializes an empty singly linked list.Initializes an empty singly linked list.f.__data = value

    @property
    def next_node(self):
    """Getter property for the data value of the node."""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
"""SinglyLinkedList class object"""

    def __init__(self):
    """initialize object"""
        self.__head = None

    def __str__(self):
        """Initializes an empty singly linked list."""
        new_list = []
        currentNode = self.__head
        while currentNode:
            new_list.append(currentNode.data)
            currentNode = currentNode.next_node
        return "\n".join(str(z) for z in sorted(new_list))

    def sorted_insert(self, value):
        """Inserts a new node with the given value in sorted order."""

        newNode = Node(value, self.__head)
        self.__head = newNode
