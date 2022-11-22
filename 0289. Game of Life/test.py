queue = []

queue.append('a')
queue.append("b")
queue.append("c")

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0)) #Oh. Of course. It takes an index to pop as arguement. pop(0) is the same as popleft for deque
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
