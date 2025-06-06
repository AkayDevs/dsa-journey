class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
def printPreOrder(head: Node) -> None:
    if head == None:
        return

    print(head.val, end="  ")
    printPreOrder(head.left)
    printPreOrder(head.right)
    
    return

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    printPreOrder(root)