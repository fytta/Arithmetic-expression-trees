import sys

""" Module with some helpful methods
to implement the arithmetic expression tree"""

def isOperator(data):

    """ Return true if data is an operator
    or false if it is not.

    :param arg: string with one character.
    :type arg: string
    :return: true o false depend of the input
    :rtype: Boolean
    """

    operators = ['+', '-', '*', '/', '^']
    if data in operators:
        return True
    else:
        return False

def precedenceOperator(op):

    """ Determine the precendence of
    the diferents operators.
    + and - : 0
    * and / : 1
    ^ : 2
    In case op isn't a operator return -1
    Higher value means higher precedence

    :param arg: operator as a string
    :type arg: string
    :return: A value specifying the precedence of the op.
    :rtype: integer
    """

    if op == '+' or op == '-':
        return 0
    elif op == '*' or op == '/':
        return 1
    elif op == '^':
        return 2
    else:
        return -1

def InfixToPostfix(infix):

    """ input string containing a valid statement in infix
    notation and returns an output string containing the same 
    statement in postfixed notation. 

    :param arg: statement in infix notation
    :type arg: string
    :return: returns an output string containing the same statement in postfixed notation.
    :rtype: string
    """
    
    output_list = [] # contains the tokens of the output expression
    operator_stack = [] # contain the operators not evaluated yet
    infix = infix.replace(" ", "")

    for t in infix:
        if t.isnumeric():
            output_list.append(t)
        elif t == '(':
            operator_stack.append(t)
        elif t == ')':
            while operator_stack[-1] != '(':
                output_list.append(operator_stack.pop())
            # end_while
            operator_stack.pop()

        elif isOperator(t):                
            if len(operator_stack) == 0:
                operator_stack.append(t)
            elif operator_stack[-1] == '(': # obtain top of the stack
                operator_stack.append(t)
            else:
                while(operator_stack and 
                        isOperator(operator_stack[-1]) and
                        (precedenceOperator(t) <= precedenceOperator(operator_stack[-1]))):
                        output_list.append(operator_stack.pop())
                # end_while
                operator_stack.append(t)
            # end_if
        # end_elif
    # end_for
    while operator_stack:
        output_list.append(operator_stack.pop())

    return output_list
