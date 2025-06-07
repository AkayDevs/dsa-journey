from queue import LifoQueue
from typing import List

class Node : 
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def iterative_postorder_traversal(head: Node) -> List[int]:
    stack1 = LifoQueue()
    stack2 = []
    stack1.put_nowait(head)

    while not stack1.empty():
        curr = stack1.get_nowait()
        stack2.append(curr.val)

        if curr.left:
            stack1.put_nowait(curr.left)
        
        if curr.right:
            stack1.put_nowait(curr.right)
    
    return stack2[:: -1]


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.left.right = Node(7)
    root.right.left.right.right = Node(8)
    print(iterative_postorder_traversal(root))