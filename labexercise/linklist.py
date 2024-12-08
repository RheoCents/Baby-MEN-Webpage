class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head: 
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_at_beginning(self):
        if self.head:
            self.removed = self.head
            self.head = self.head.next
            if self.head is None: 
                self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_at_end(self):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            if current_node.next ==  self.tail:
                self.tail = current_node
                self.removed = current_node.next
                current_node.next = None
            current_node = current_node.next
    
    def remove_at(self):
        if self.removed != None:
            removed_data = self.removed
            self.removed = None
            return removed_data
        else:
            return "Null"
        
    def list_LinkedList(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result