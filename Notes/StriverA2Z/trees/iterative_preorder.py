from queue import LifoQueue

class Node:
    def __init__(self, val):
        self.val = val 
        self.left : Node = None
        self.right : Node = None

def preorder_iterative(head: Node) -> None:
    if head == None:
        return
    
    s = LifoQueue()
    s.put_nowait(head)

    while not s.empty():
        cur_node = s.get_nowait()
        print(cur_node.val)
        
        if cur_node.right:
            s.put_nowait(cur_node.right)
        if cur_node.left:
            s.put_nowait(cur_node.left)


    return

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.right.left = Node(5)
    root.left.right.right = Node(6)
    preorder_iterative(root)