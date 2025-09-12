# Implement Queue Using Array/List

'''
Input: Queries = 1 3 2 2 1 4   
Output: 3 -1
Explanation: For query 1 3 the queue will be {3} 2 popped element will be 3 the queue will be empty 2 there is no element in the queue and hence -1 1 4 the queue will be {4}. 
'''

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print ("dequeue from empty queue")
            return 
        x = self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items) == 0:
            print ("Cannot peek Queue is empty")
            return
        return self.items[0]
    
    def rear(self):
        if len(self.items) == 0:
            print ("Cannot peek Queue is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Dequeued:", queue.dequeue())   # prints dequeued value
print("Front element:", queue.front())  # prints front
print("Rear element:", queue.rear())    # prints rear
print("Queue size:", queue.size())      # prints size