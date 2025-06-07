class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

max_diameter = 0

def diameter_of_binary_tree(head: Node) -> int:
    if head == None:
        return 0
    
    lh = diameter_of_binary_tree(head.left)
    rh = diameter_of_binary_tree(head.right)

    global max_diameter
    max_diameter = max(max_diameter, lh + rh)
    
    return 1 + max(lh, rh)
    
if __name__ == "__main__":
    root = Node(9)
    root = Node(5, root)
    root = Node(4, root)
    root = Node(3, root, Node(6, None, Node(7, None, Node(8))))
    root = Node(1, Node(2), root)
    diameter_of_binary_tree(root)
    print(max_diameter)