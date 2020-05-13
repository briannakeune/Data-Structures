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
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
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

    def __str__(self):
        return str(self.value)


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
            self.tail = listed_node

        # what if it isn't
        else:
            prev_head = self.head
            # handle the old head's previous pointer
            prev_head.insert_before(value)
            # declaring that the previous head's prev attr is now the head
            self.head = prev_head.prev
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        removed_node = self.head.value
        # if dll len is 0
        if self.head is None and self.tail is None:
            # could be an exception?
            return None
        # if dll is len 1
        elif self.head is self.tail:
            self.head, self.tail = None, None
            self.length -= 1
            return removed_node
        # if dll is > len 1
        else:
            self.head = self.head.next
            self.length -= 1
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
        self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # if dll is empty
        if self.head is None and self.tail is None:
            # maybe I should turn this into an exception
            return None
        # if dll is length 1
        elif self.tail is self.head:
            removed_node = self.tail.value
            self.head, self.tail = None, None
            self.length -= 1
            return removed_node
        # if dll is > 1
        else:
            # holding on to data from tail
            removed_node = self.tail.value
            # remove the list's current tail node
            self.tail = self.tail.prev
            self.length -= 1
            # returns the value of the removed node
            return removed_node

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return None
        else:
            # holding moving nodes data
            node_to_move = node
            # making a link bewteen node_to_move prev, next attrs
            node_to_move.prev.next, node_to_move.next.prev = node_to_move.next, node_to_move.prev

            # making node to move the new head of the list
            node.add_to_head(node_to_move)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return None
        else:
            # holding moving node's data
            node_to_move = node
            # making a link between node's prev, next attrs
            node_to_move.prev.next, node_to_move.next.prev = node_to_move.next, node_to_move.prev
            # making node to move the new tail of the list
            node.add_to_tail(node_to_move)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # the remove functions on the dll class already subtract from length,
        # the node's delete does not have access to the length so we must remove
        if node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        # if list is empty
        if len(self) is 0:
            return None
        else:
            sorted_list = sorted([i.value for i in self])
            return sorted_list[-1]

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        return str(self)
