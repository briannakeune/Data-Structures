class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in the node
        self.next_node = new_next


"""
creating a linked list by hand
ll = Node(1)
ll.next_node = Node(2)
ll.next_node.next_node = Node(3)
ll.next_node.next_node.next_node = Node(4)

or

ll_1 = Node(1)
ll_2 = Node(2)
ll_3 = Node(3)
ll_4 = Node(4)
ll_1.set_next(ll_2)
ll_2.set_next(ll_3)
ll_3.set_next(ll_4)

"""


class LinkedList:
    def __init__(self):
        # we'd want access to the 'head'
        # which is the first node in the list
        # head is not declared until invoked
        self.head = None

    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)
        # what if the list is empty?
        # value is the actual value, and hasn't been wrapped in Node yet
        # then create that as the head
        if not self.head:
            self.head = new_node

        # what if the list is not empty?
        else:
            current = self.head
            # we can get to the last node in the list by traversing it
            while current.get_next_node() is not None:
                current = current.get_next_node()
            # we're at the end of the linked list
            # append new_node to last node in the node
            current.set_next(new_node)

    def add_to_head(self, value):
        # still respecting the order of the linked list
        # head must be moved to secondary position of linked list
        # current.head -> next node
        # next node -> current.head.next_node.next_node
        # value -> current.head
        # ^ proccess must happen through all of the linked lists nodes.

        # takes value and turns it into new head
        # and places the previous list as the as the new next node?
        # ^ I'll put this in python tutor later to visual more
        self.head = Node(value, self.head)

    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it is not empty?
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next_node()
            return value
