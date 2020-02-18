# Arithmetic-expression-trees

It is a binary tree that allows the representation of the arithmetic expression (in infixed notation) with or without parenthesis. In order to build this type of tree, it is first necessary to transform the arithmetic expression in infix notation to postfix notation. In infixed notation, operators appear between the middle of their two operands (e.g. 3 + 4). In postfixed notation, operators always appear after their two operands (e.g. 3 4 +).  Once we have the expression in postfixed notation, we can build the expression tree.  Finally, we must evaluate an expression tree to obtain the final result.

Classes implemented:
* BinaryTreeNode: To create the nodes of the binary tree
* BinaryTree: To build the binary tree

Modules:
* Operations: It has helpful method to build the tree

Python version 3.7
