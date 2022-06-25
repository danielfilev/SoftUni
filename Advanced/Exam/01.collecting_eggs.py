from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = [int(x) for x in input().split(', ')]

filled_boxes = 0

while eggs and papers:

    while eggs and eggs[0] <= 0:
        eggs.popleft()

    if not eggs:
        break

    if not papers:
        break

    current_paper = papers.pop()
    current_egg = eggs.popleft()

    if current_egg == 13:
        current_paper, papers[0] = papers[0], current_paper
        papers.append(current_paper)
    if current_egg != 13 and current_egg + current_paper <= 50:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    eggs_string = ", ".join(str(x) for x in eggs)
    print(f'Eggs left: {eggs_string}')
if papers:
    papers_string = ", ".join(str(x) for x in papers)
    print(f'Pieces of paper left: {papers_string}')
