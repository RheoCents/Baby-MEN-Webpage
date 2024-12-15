# stack.py

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
            steps.append(''.join(output))
        elif token == '(':
            ops.push(token)
        elif token == ')':
            while ops.peek() != '(':
                popped = ops.pop()
                output.append(popped)
                steps.append(''.join(output))
            ops.pop()  # Pop the '('
        else:  # Operator
            while (ops.peek() is not None and precedence(ops.peek()) >= precedence(token)):
                popped = ops.pop()
                output.append(popped)
                steps.append(''.join(output))
            ops.push(token)


    while ops.peek() is not None:
        popped = ops.pop()
        output.append(popped)
        steps.append(''.join(output))
        
    def generated_list():
        for step in steps:
            yield step

    # Convert generator to list before returning
    return ''.join(output), list(generated_list())


