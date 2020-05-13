from list_node import ListNode

"""
List nodes have method options:
    insert_before()
    insert_after()
    remove()
"""


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
        # update length
        self.length += 1
        # wraps the given value in a ListNode
        new_node = ListNode(value)
        # no list has started
        if self.head is None and self.tail is None:
            self.head, self.tail = new_node, new_node
        else:
            # prev's head data
            prev_head = self.head
            # inserts it as the new head
            self.head = new_node
            # handle the previous head's prev pointer
            # to point to the new head
            prev_head.prev = self.head

    """
    Deletes the current node of that is classified as the head,
    while making the head's previous value the new head
    """

    def remove_from_head(self):
        # update self.length
        self.length -= 1
        # hold head data
        to_remove = self.head
        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            # removes the head value
            self.head.remove()
            # updating the list head to the removed head's next value
            self.head = to_remove.next
        # returns the value of the removed node
        return to_remove.value

    """
    Takes a value and sets it to the tail position of list,
    while moving previous tail to the value's/new tail's next position
    """

    def add_to_tail(self, value):
        # updating self.length
        self.length += 1
        # wraps the given value in a ListNode
        new_node = ListNode(value)
        # no head, or tail, should be added to both
        if self.head is None and self.tail is None:
            self.head, self.tail = new_node, new_node
        else:
            # prev's tail data
            prev_tail = self.tail
            # insert is as the new tail
            self.tail = new_node
            # handle previous tails next pointer
            # to point to new tail
            prev_tail.next = self.tail

    """
    Deletes the current node of that is classified as the tail,
    while making the tail's previous value the new tail
    """

    def remove_from_tail(self):
        # update self.length
        self.length -= 1
        # hold tail data
        to_remove = self.tail
        # handling if length is 1
        if self.tail is self.head:
            self.head, self.tail = None, None
        else:
            # removes the tail value
            self.tail.remove()
            # updating the list tail to the removed tail's prev value
            # returns the value of the removed node
        return to_remove.value

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
        # update self.length
        self.length -= 1
        # removes a node from the list
        node.delete()
        # handles cases where the node was the head or the tail

    """Returns the highest value currently in the list"""

    def get_max(self):
        # starting place for loop
        # if list is empty
        if len(self) is 0:
            return None
        else:
            sorted_list = sorted([i.value for i in self])
            return sorted_list[-1]

    def __iter__(self):
        current = self.head
        # list to sort
        a_list = sorted([])
        while current is not None:
            # while there are nodes, append the current not to list
            a_list.append(current.value)
            # move to next
            yield current
            current = current.next
        # sort the list and return the last, max element
        return (a_list[-1])

    def __str__(self):
        return str(self)
