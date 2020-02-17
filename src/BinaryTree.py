import BinaryTreeNode as btn
from Operation import *

class BinaryTree:     

    """ Class used to implement a binary tree to build
    an arithmetic expression tree.

    Class with the operations need to build the 
    binary tree and go through it and evaluate it
    to get the final result about the 
    arithmethic expression
    """

    root = None
    postorder_tree = []
    n_nodes = 0

    def setRoot(self, node):
        self.root = self.newNode(node)

    def getRoot(self):
        return self.root

    def newNode(self, data):
        return btn.BinaryTreeNode(data)
    

    def getNumNodes(self):
        return self.n_nodes
    
    def setNumNodes(self, n_nodes):
        self.n_nodes = n_nodes

    def toTree(self, infix):

        """ From an input string containing a valid expression 
        in postfixed notation 
        and returns a tree representing that expression.

        :param arg: string in postfix notation
        :type arg: String
        :return: the root node
        :rtype: BinaryTreeNode
        """

        nodes_lst = []
        infix = InfixToPostfix(infix)
        self.setNumNodes(len(infix))
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
        self.postorder(self.getRoot())      
        return self.getRoot()
    
    def postorder(self, node):  

        """Go through the tree in postorder and save 
        the data of the nodes in a postorder_tree variable list

        :param arg: a tree node
        :type arg: BinaryTreeNode
        :return: A list in postorder
        :rtype: list
        """ 

        if node != None:
            self.postorder(node.getRight()) 
            self.postorder(node.getLeft())
            self.postorder_tree.append(node.getData())
        else: 
            return self.postorder_tree
    
    def eval(self, node):

        """ Go through the tree in post-order and apply the 
        operations in the same order as the nodes are visited.
        Process a binary expression tree to obtain the final result of 
        the arithmetic expression

        :param arg: a tree node
        :type arg: BinaryTreeNode
        :return: A list in postorder
        :rtype: The final result of the arithmetic expression.
        """

        result = -1.0
        if isOperator(node.getData()):
            op = node.getData()

            if op == '+':
                result = self.eval(node.getLeft()) + self.eval(node.getRight())
            elif op == '-':
                result = self.eval(node.getLeft()) - self.eval(node.getRight())                
            elif op == '*':
                print(node.getLeft().getData(),node.getRight().getData() )
                result = self.eval(node.getLeft()) * self.eval(node.getRight())   
            elif op == '/':
                result = self.eval(node.getLeft()) / self.eval(node.getRight())
            elif op == '^':
                result = pow(self.eval(node.getLeft()), self.eval(node.getRight()))
        else:
            result = float(node.getData())
        return result

if __name__ == "__main__":
    tree = BinaryTree()
    tree.toTree("(2+3)*4")
    print(tree.postorder_tree)
    print(tree.eval(tree.getRoot()))     