from collections import deque

deque_ = deque()

deque_.append(1)
deque_.append(2)
deque_.append(3)

print(deque_) # [1, 2, 3]

if deque_:
    print("deque is not empty")

if deque_:
    left = deque_.popleft()
    print(left) # 1
    right = deque_.pop()
    print(right) # 3

print(deque_)

if not deque_:
    print("deque is empty")