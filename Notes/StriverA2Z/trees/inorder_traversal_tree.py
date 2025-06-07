class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printInorder(head : Node):
    if head == None:
        return

    printInorder(head.left)
    print(head.val, end=" ")
    printInorder(head.right)

    return
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right = Node(6)
    printInorder(root)