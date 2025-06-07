class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printPostorder(head : Node):
    if head == None:
        return

    printPostorder(head.left)
    printPostorder(head.right)
    print(head.val, end=" ")

    return
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right = Node(6)
    printPostorder(root)