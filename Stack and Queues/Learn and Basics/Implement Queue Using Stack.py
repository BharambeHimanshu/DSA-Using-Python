# Implement Queue(FIFO) Using  2 Stack(LIFO)

class MyQueue:
    def __init__(self):
        # Two stacks: in_stack (for push), out_stack (for pop/peek)
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Add to in_stack (end of queue)
        self.in_stack.append(x)

    def pop(self) -> int:
        # Pop from out_stack (front of queue)
        self.peek()  # Ensure out_stack has the current items
        return self.out_stack.pop()

    def peek(self) -> int:
        # Get the front element
        if not self.out_stack:
            # Transfer all from in_stack to out_stack if needed, reversing order
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return not self.in_stack and not self.out_stack

queue = MyQueue()
queue.push(10)
queue.push(20)
queue.push(30)
print("element popped : ",queue.pop())
print("Top element", queue.peek())
queue.push(50)
print("element popped : ",queue.pop())
print("Top element", queue.peek())