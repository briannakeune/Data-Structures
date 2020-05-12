"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value  # current node in list
        self.prev = prev  # stores, previous node
        self.next = next  # stores next node

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is pointing to."""

    """
    a_saved_node = ListNode(1)
    a_saved_node.insert_after(2)
    """

    def insert_after(self, value):
        # saving next value
        current_next = self.next
        # setting the new next value of self...
        # (what is self pointing to, the entirety of which node value? value param?)
        # to a new list node, where self = value?, value = prev node value, and the prev = the original next value?
        self.next = ListNode(value, self, current_next)
        # if self.next exists
        if current_next:
            # set the next nodes, prev attr to itself?
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is pointing to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # wraps the given vlaue in a ListNode
        listed_node = ListNode(value)

        # what if self.head is None
        if self.head is None and self.tail is None:
            # inserts it as the new head of the list
            self.head = listed_node

        # what if it isn't
        else:
            prev_head = self.head
            self.head = listed_node
        # handle the old head's previous pointer
            listed_node.next = prev_head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # remove the lists current head node
        removed_node = self.head
        # making the curent head's next node the new head of the list
        self.head = self.head.next
        # returns the value of the removed node
        return removed_node

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # saving prev_tail to handle pointer
        prev_tail = self.tail
        # wraps the given value in a listnode, and adds self.tail to prev spot
        new_tail = ListNode(value, self.tail)
        # inserts value as new tail of the list
        self.tail = new_tail
        # handles prev_tails next pointer
        # to point to new tail
        prev_tail.next = self.tail

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # declaring which node I am removing
        removed_node = self.tail
        # remove the list's current tail node
        # making the current tail's previous node the new tail
        self.tail = self.tail.prev
        # returns the value of the removed node
        return removed_node

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # holding moving nodes data
        node_to_move = node
        # making a link bewteen node_to_move prev, next attrs
        node_to_move.prev.next, node_to_move.next.prev = node_to_move.next, node_to_move.prev
        """"""
        # making node to move the new head of the list
        node.add_to_head(node_to_move)
        """"""

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        print('NODE: ', node.value)
        if node is self.tail:
            return None
        else:
            # holding moving node's data
            node_to_move = node
            # making a link between node's prev, next attrs
            node_to_move.prev.next, node_to_move.next.prev = node_to_move.next, node_to_move.prev
            """"""
            # making node to move the new tail of the list
            node.add_to_tail(node_to_move)
            """"""

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        removed_node = node
        if node is self.head:
            self.head = node.next
        elif node is self.tail:
            self.tail = node.prev
        else:
            node.prev.next, node.next.prev = node.next, node.prev

        return removed_node

    """Returns the highest value currently in the list"""

    def get_max(self):
        # starting place for loop
        current = self.head
        # list to sort
        a_list = sorted([])
        while current is not None:
            # while there are nodes, append the current not to list
            a_list.append(current.value)
            # move to next
            current = current.next
        # sort the list and return the last, max element
        return (a_list[-1])
