import BinaryTreeNode as btn

class BinaryTree:

    def __init__(self, data=None):
        self.root = btn.BinaryTreeNode(data)
        self.leftc = None
        self.rightc = None

    def setRoot(self, data):
        self.root.setData(data)

    def getRoot(self):
        return self.root

    def newNode(self, data):
        return btn.BinaryTreeNode(data)

bt = BinaryTree(5)
bt.getRoot().setLeft(bt.newNode(3))
print(bt.getRoot().getData(), bt.getRoot().getLeft().getData())
