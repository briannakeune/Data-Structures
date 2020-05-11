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


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # returns size attr for the declared stack
        return self.size

    def push(self, value):
        # adds value to the end of the stack
        self.storage.append(value)

        # update size when added
        self.size = self.size + 1

        # does not need to return what is stored

    def pop(self):
        # what if there is no stack
        if not self.storage:
            return None
        # what if there is someone in stack
        else:
            # stacks return elements that we're removed
            # saving it for later
            value = self.storage[-1]
            # deleting last value from storage
            del self.storage[-1]

            # has to remove whatever at the end of the stack
            self.size = self.size - 1
        return value
