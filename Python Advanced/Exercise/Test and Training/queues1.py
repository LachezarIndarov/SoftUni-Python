# Queues - Опашка -  FIFO - Стека си има готова структура в Python

from collections import deque
q = deque
# Enqueue - push,add
q.append(1) # appendRight - default
q.appendleft(2)

# Dequeue - pop,remove
q.pop(0) #very wrong
q.pop # popRight() - default
q.popleft()

# Peek - print
print(q[0])

# Count