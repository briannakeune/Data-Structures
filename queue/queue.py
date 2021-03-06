"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add a value to be the last node on ll
        self.storage.add_to_end(value)
        # update the size attr
        self.size = self.size + 1

    def dequeue(self):
        # if list is empty then return nothing
        if not self.storage.head:
            return None
        else:
            # remove first element from ll
            value = self.storage.remove_from_head()
            # update the size attr
            self.size = self.size - 1
            return value
