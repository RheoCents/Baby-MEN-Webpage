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
    if op == '^':  
        return 3
    return 0

def infix_to_postfix(expression):
    spaceless = expression.replace(" ", "")
    ops = Stack()
    output = []
    steps = [] 

    for token in spaceless:
        if token.isalnum(): 
            output.append(token)
            steps.append(''.join(output))  # Record the step after adding an operand
        elif token == '(':
            ops.push(token)
        elif token == ')':
            while ops.peek() != '(':
                popped = ops.pop()
                output.append(popped)
            ops.pop()  
            steps.append(''.join(output))  # Record the step after processing a closing parenthesis
        else: 
            while (ops.peek() is not None and precedence(ops.peek()) >= precedence(token)):
                popped = ops.pop()
                output.append(popped)
            ops.push(token)
            steps.append(''.join(output))  # Record the step after processing an operator

    while ops.peek() is not None:
        popped = ops.pop()
        output.append(popped)
        steps.append(''.join(output))  # Record the step after popping remaining operators

    return ''.join(output), steps

def infix_to_prefix(expression):
    spaceless = expression.replace(" ", "")
    reversed_expr = spaceless[::-1]
    reversed_expr = reversed_expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    ops = Stack()
    output = []
    prefix_steps = [] 

    for token in reversed_expr:
        if token.isalnum(): 
            output.append(token)
        elif token == '(':
            ops.push(token)
        elif token == ')':
            while ops.peek() != '(':
                popped = ops.pop()
                output.append(popped)
            ops.pop()  
        else:
            while (ops.peek() is not None and precedence(ops.peek()) > precedence(token)):
                popped = ops.pop()
                output.append(popped)
            ops.push(token)

        prefix_steps.append(''.join(output[::-1]))

    while ops.peek() is not None:
        popped = ops.pop()
        output.append(popped)
        prefix_steps.append(''.join(output[::-1]))  

    prefix_expression = ''.join(output[::-1]) 

    return prefix_expression, prefix_steps
