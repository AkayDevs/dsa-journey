from typing import List
from queue import LifoQueue

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def traversal_postorder_single_stack(head: Node) -> List[int]:
    stack = LifoQueue()
    traversal_order = []
    current: Node = head

    while current is not None or not stack.empty():
        if current is not None:
            stack.put_nowait(current)
            current = current.left
        else :
            temp = stack.queue[-1].right
            if temp is None:
                temp_node = stack.get_nowait()
                traversal_order.append(temp_node.val)
                while not stack.empty() and stack.queue[-1].right == temp_node:
                    temp_node = stack.get_nowait()
                    traversal_order.append(temp_node.val)
            else:
                current = temp

    return traversal_order

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.right = Node(4)
    root.left.left.right.right = Node(5)
    root.left.left.right.right.right = Node(6)
    root.right = Node(7)
    root.right.left = Node(8)
    print(traversal_postorder_single_stack(root))