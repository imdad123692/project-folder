#task 1

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)
    
stack = Stack()
print("Stack after initialization:", stack)
stack.push(1)
print("Stack after pushes:", stack)
stack.push(2)
print("Stack after pushes:", stack)
stack.push(3)
print("Stack after pushes:", stack)
print("Popped item:", stack.pop())
print("Stack after pop:", stack)
print("Peek item:", stack.peek())
print("Stack size:", stack.size())

#task 2

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

queue = Queue()
print("Queue after initialization:", queue)
queue.enqueue(1)
print("Queue after enqueue:", queue)
queue.enqueue(2)
print("Queue after enqueues:", queue)
queue.enqueue(3)
print("Queue after enqueues:", queue)
print("Dequeued item:", queue.dequeue())
print("Queue after dequeue:", queue)
print("Peek item:", queue.peek())
print("Queue size:", queue.size())

#task 3

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def test_binary_search():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

test_binary_search()

