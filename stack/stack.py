"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # returns size attr for the declared stack
        return self.size

    def push(self, value):
        # adds value to the end of the stack
        self.storage.add_to_head(value)

        # update size when added
        self.size = self.size + 1

        # does not need to return what is stored

    def pop(self):
        # what if there is no stack
        if not self.storage.head:
            return None
        # what if there is something in stack
        else:
            # stacks return elements that we're removed
            # saving it for later
            value = self.storage.head.get_value()
            # deleting last value from storage
            # has to remove whatever at the top most recently added of the stack
            self.storage.remove_from_head()
            # remove value amt from size
            self.size = self.size - 1
        return value
