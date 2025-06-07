from typing import List
from queue import LifoQueue

class Node:

    def __init__(self, val):
        self.data = val 
        self.left = None
        self.right = None

def iterative_inorder(head: Node) -> List[int]:
    ans = []
    stack = LifoQueue()
    curr = root

    while curr is not None or not stack.empty():
        
        # Reach the left most Node of the curr Node
        while curr is not None:
            
            # Place pointer to a tree node on
            # the stack before traversing
            # the node's left subtree
            stack.put_nowait(curr)
            curr = curr.left

        # Current must be None at this point
        curr = stack.get_nowait()
        ans.append(curr.data)

        # we have visited the node and its
        # left subtree. Now, it's right
        # subtree's turn
        curr = curr.right

    return ans
            

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.right.left = Node(5)
    root.left.right.right = Node(6)
    print(iterative_inorder(root))