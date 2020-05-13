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
