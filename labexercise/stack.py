class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = popped_node.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':  # Exponentiation
        return 3
    return 0

def infix_to_postfix(expression):
    spaceless = expression.replace(" ", "")
    ops = Stack()
    output = []
    steps = [] 

    for token in spaceless:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            ops.push(token)
        elif token == ')':
            while ops.peek() != '(':
                popped = ops.pop()
                output.append(popped)
            ops.pop()  # Pop the '('
        else:  # Operator
            while (ops.peek() is not None and precedence(ops.peek()) >= precedence(token)):
                popped = ops.pop()
                output.append(popped)
            ops.push(token)

    while ops.peek() is not None:
        popped = ops.pop()
        output.append(popped)

    # Capture the steps in the desired format
    for item in reversed(output):  # Reverse the order to match the expected output
        steps.append(item)

    return ''.join(output), steps

def postfix_to_infix(expression):
    spaceless = expression.replace(" ", "")
    stack = Stack()
    steps = []

    for token in spaceless:
        if token.isalnum():  # Operand
            stack.push(token)
        else:  # Operator
            op2 = stack.pop()  # The second operand (right side)
            op1 = stack.pop()  # The first operand (left side)
            new_expr = f"{op1}{token}{op2}"
            stack.push(new_expr)
            steps.append(new_expr)  # Only append the current infix expression

    # Return the final infix expression and the steps
    return stack.pop(), steps

def infix_to_prefix(expression):
    spaceless = expression.replace(" ", "")
    # Reverse the expression
    reversed_expr = spaceless[::-1]
    
    # Replace '(' with ')' and vice versa
    reversed_expr = reversed_expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    ops = Stack()
    output = []
    steps = []

    for token in reversed_expr:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            ops.push(token)
        elif token == ')':
            while ops.peek() != '(':
                popped = ops.pop()
                output.append(popped)
            ops.pop()  # Pop the '('
        else:  # Operator
            while (ops.peek() is not None and precedence(ops.peek()) > precedence(token)):
                popped = ops.pop()
                output.append(popped)
            ops.push(token)

    while ops.peek() is not None:
        popped = ops.pop()
        output.append(popped)

    # Reverse the output to get the prefix expression
    prefix_expression = ''.join(output[::-1])

    # Capture the steps
    for item in reversed(prefix_expression):  # Reverse to match the step format
        steps.append(item)

    return prefix_expression, steps
