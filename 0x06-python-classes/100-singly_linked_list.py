#!/usr/bin/python3


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (int): The data value stored in the node.
        next_node (Node): The reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
            data (int): The data value to be stored in the node.
            next_node (Node, optional): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data value of the node.

        Returns:
            int: The data value stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Args:
            value (int): The data value to be set.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the reference to the next node.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Args:
            value (Node): The next node to be set.

        Raises:
            TypeError: If the provided value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a node of a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty SinglyLinkedList instance.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The data value of the new Node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Generates a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
