class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty, cannot dequeue")
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue size:", q.size())  

print("Dequeued item:", q.dequeue()) 

print("Queue size after dequeue:", q.size())  

print("Is the queue empty?", q.is_empty())  

q.dequeue()
q.dequeue()

print("Is the queue empty now?", q.is_empty())  