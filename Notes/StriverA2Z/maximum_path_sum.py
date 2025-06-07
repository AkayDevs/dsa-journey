class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

max_sum = 0

def maximum_path_sum(head: Node) -> int:
    global max_sum

    if head == None:
        return 0
    
    lmax = max(0, maximum_path_sum(head.left))
    rmax = max(0, maximum_path_sum(head.right))

    node_sum = head.val + lmax + rmax
    max_sum = max(max_sum, node_sum)

    return head.val + max(lmax, rmax)
    
if __name__ == "__main__":
    root = Node(-10, Node(9), Node(20, Node(15), Node(7)))
    maximum_path_sum(root)
    print(max_sum)