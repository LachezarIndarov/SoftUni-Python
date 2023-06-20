from collections import deque

q = deque([1,2,3,4,5,6,7,8,9])
print(q) # deque([1, 2, 3, 4, 5, 6, 7, 8, 9])


for i in range(4):
    q.append((q.popleft()))

print(q) # deque([5, 6, 7, 8, 9, 1, 2, 3, 4])



q = deque([1,2,3,4,5,6,7,8])
print(q) # deque([1, 2, 3, 4, 5, 6, 7, 8])
q.rotate(4)
print(q) # deque([5, 6, 7, 8, 1, 2, 3, 4])