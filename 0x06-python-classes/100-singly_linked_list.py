#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The next_node property."""
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):

        self.__head = None

    def __str__(self):

        new_list = []
        currentNode = self.__head
        while currentNode:
            new_list.append(currentNode.data)
            currentNode = currentNode.next_node
        return "\n".join(str(z) for z in sorted(new_list))

    def sorted_insert(self, value):

        newNode = Node(value, self.__head)
        self.__head = newNode

