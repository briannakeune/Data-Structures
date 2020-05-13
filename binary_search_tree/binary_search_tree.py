class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # wrap value into Node
        new_node = BSTNode(value)
        # value = new_node.value
        # should I check if this value is already in the tree?
        # if it's in the tree return none
        if self.contains(value):
            return None
        # compare value to root for placement
        if value < self.value:
            # check self.left, if no value, place there
            if not self.left:
                self.left = new_node
            # else continue to find next empty spot.
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        BSTNode(target)
        value = self.value
        # start searching at root,
        if target is value:
            return True
        # compare target again self
        # choose a direction based
        # on compared value
        # reiterate until target matches self,
        # or we hit a leaf
        if target < value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # this should have to go through only the right path?
        # i'll have to draw this one out
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    """Part 2 -----------------------"""

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
