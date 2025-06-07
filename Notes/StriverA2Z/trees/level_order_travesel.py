from queue import Queue
from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order_traversal(head: Node) -> None:
    ans = []
    q = Queue()
    q.put_nowait(head)

    while not q.empty():
        nodes: Node = q.get_nowait()
        new_nodes: List[Node] = []
        nums_list = []
        for node in range(len(nodes)):
            if node.left != None:
                new_nodes.append(node.left)
            
            if node.right != None:
                new_nodes.append(node.right)
            
            nums_list.append(node.val)
        
        ans.append(nums_list)
        if len(new_nodes) > 0:
            q.put_nowait(new_nodes)

if __name__ == "__main__":
    pass