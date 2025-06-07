class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_balanced_binary_tree(head: Node) -> int: 
    if head == None:
        return 0
    
    lh = check_balanced_binary_tree(head.left)
    if lh == -1:
        return -1
    
    rh = check_balanced_binary_tree(head.right)
    if rh == -1 :
        return-1

    if abs(lh - rh) > 1:
        return -1
    
    return 1 + max(lh, rh)
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.left.right = Node(5)
    root.right.left.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.right = Node(8)
    ans = check_balanced_binary_tree(root)
    print(True if ans != -1 else False)