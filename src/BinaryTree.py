import BinaryTreeNode as btn
from Operation import *

class BinaryTree:     

    root = None
    def setRoot(self, node):
        self.root = self.newNode(node)

    def getRoot(self):
        return self.root

    def newNode(self, data):
        return btn.BinaryTreeNode(data)

    def toTree(self, postfix):
        nodes_lst = []
        infix = postfixToInfix(postfix)
        
        for t in infix:
            if t.isnumeric():
                nodes_lst.append(self.newNode(t))
            elif isOperator(t):
                aux_node = self.newNode(t)
                aux_node.setLeft(nodes_lst.pop())
                aux_node.setRight(nodes_lst.pop())
                nodes_lst.append(aux_node)
                
        # end_for
        self.root = nodes_lst.pop()
        return self.getRoot()
    
    def preorder(self, node):       
        if node != None:
            print(node.getData())
            self.preorder(node.getLeft())
            self.preorder(node.getRight()) 

    def inorder(self, node):       
        if node != None:
            self.preorder(node.getLeft())
            print(node.getData())
            self.preorder(node.getRight()) 

    def postorder(self, node):       
        if node != None:
            self.preorder(node.getLeft())
            self.preorder(node.getRight()) 
            print(node.getData())

     