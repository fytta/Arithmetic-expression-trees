import sys

def isOperator(data):
    operators = ['+', '-', '*', '/', '^']
    if data in operators:
        return True
    else:
        return False

def precedenceOperator(op):
    if op == '+' or op == '-':
        return 0
    elif op == '*' or op == '/':
        return 1
    elif op == '^':
        return 2
    else:
        return -1

def postfixToInfix(postfix): #2+3*4 -> 2 3 4 * +
    # Variables
    output_list = [] # contains the tokens of the output expression
    operator_stack = [] # contain the operators not evaluated yet
    postfix = postfix.replace(" ", "")

    for t in postfix:
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
