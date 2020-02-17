class BinaryTreeNode:

    """ Class to create a binary tree nodes with
    left and right childs
    """

    def __init__(self, data):
        self.data = data
        self.left = None # Node
        self.right = None # Node

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setRight(self, child):
        self.right = child
        
    def setLeft(self, child):
        self.left = child  

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right