from collections import deque

eggs_deque = deque(map(int, input().split(", ")))
papers_stack = list(map(int, input().split(", ")))


boxes = 0

while eggs_deque and papers_stack:
    egg = eggs_deque.popleft()





    if egg <= 0:
        continue

    if egg == 13:

        papers_stack[0], papers_stack[len(papers_stack)-1] = papers_stack[len(papers_stack)-1], papers_stack[0]
        continue

    paper = papers_stack.pop()

    if egg + paper <= 50:
        boxes += 1



if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")




if eggs_deque:
    print(f"Eggs left: ",end="")
    print(', '.join([str(i) for i in eggs_deque]))
elif papers_stack:
    print(f"Pieces of paper left: ", end="")
    print(', '.join([str(i) for i in papers_stack]))