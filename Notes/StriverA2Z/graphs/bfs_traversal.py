from queue import Queue
from typing import List

# Can also be implemented using default dict
def create_adjacency_list(n : int, edges: List[List[int]]):
    adjacency_list = {}
    for i in range(1, n + 1):
        adjacency_list[i] = []
    
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    return adjacency_list

def bfs_traverse(n, adjacency_dict, starting_node) -> List[int]:
    q = Queue()
    visited = [0] * (n + 1)
    traversal_order = []

    q.put_nowait(starting_node)
    # visited[starting_node] = 1
    # traversal_order.append(starting_node)

    while(not q.empty()):
        cur = q.get_nowait()
        if visited[cur] != 1:
            traversal_order.append(cur)
            visited[cur] = 1
            for neighbour in adjacency_dict[cur]:
                q.put_nowait(neighbour)
    
    return traversal_order

if __name__ == "__main__":
    n, m, starting_node = map(int, input().split())
    edges = []
    for i in range(m):
        node_from, node_to = map(int, input().split())
        edges.append([node_from, node_to])

    adj_list = create_adjacency_list(n, edges)
    print(bfs_traverse(n, adj_list, starting_node))


    