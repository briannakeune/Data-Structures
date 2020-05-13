class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """
    Inserts a given value to be the next of the node invoked on, 
    while creating given value as a class of node
    """

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """
    Inserts a given value to be the prev of the node invoked on,
    while creating given value as a class of node
    """

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """
    Removes node invoke on, 
    and links up that nodes prev, and next 
    to create a continuous linked list
    """

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Takes a value and sets it to the head position of list,
    while moving previous head to the value's/new head's next position
    """

    def add_to_head(self, value):
        # wraps the given value in a ListNode
        # inserts it as the new head
        # handle the previous head's prev pointer
        # to point to the new head
        pass

    """
    Deletes the current node of that is classified as the head,
    while making the head's previous value the new head
    """

    def remove_from_head(self):
        # removes the head value
        # updating the list head to the removed head's next value
        # returns the value of the removed node
        pass

    """
    Takes a value and sets it to the tail position of list,
    while moving previous tail to the value's/new tail's next position
    """

    def add_to_tail(self, value):
        # wraps the given value in a ListNode
        # insert is as the new tail
        # handle previous tails next pointer
        # to point to new tail
        pass

    """
    Deletes the current node of that is classified as the tail,
    while making the tail's previous value the new tail
    """

    def remove_from_tail(self):
        # removes the tail value
        # updating the list tail to the removed tail's prev value
        # returns the value of the removed node
        pass

    """
    Takes any list node and moves it to become the
    head of the list,
    if given the head node to move to the head
    will recieve a value error
    """

    def move_to_front(self, node):
        # removes the input node
        # inserts input node as new head of list
        pass

    """
    Takes any list node and moves it to become the
    tail of the list,
    if given the tail node to move to the tail
    will recieve a value error
    """

    def move_to_end(self, node):
        # remove the input node from it's current spot
        # inserts input node as new tail of list
        pass

    """
    Removes a node from any where in the dll,
    while keeping the rest of the list intact, 
    and updating any broken links, 
    or updating the head, or tail flags
    """

    def delete(self, node):
        # removes a node from the list
        # handles cases where the node was the head or the tail
        pass

    """Returns the highest value currently in the list"""

    def get_max(self):
        # write todo here
        pass
