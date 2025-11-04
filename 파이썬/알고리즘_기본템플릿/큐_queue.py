from collections import deque

queue = deque()

queue.append(1)
print(queue) # [1]

queue.append(2)
print(queue) # [1, 2]

print(queue.popleft()) # [1]
print(queue) # [2]

queue.append(1)
print(queue) #[2, 1]

if queue:
    first = queue.popleft() # 2 
    print(first) # [1]

if not queue:
    print("queue is empty")