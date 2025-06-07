from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_max_height(head: Node) -> int:
    if head == None:
        return 0

    return 1 + max(get_max_height(head.left), get_max_height(head.right))



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.left.right = Node(5)
    root.right.left.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.right = Node(8)
    print(get_max_height(root))