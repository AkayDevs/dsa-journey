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

traversal_order = []

def dfs_traverse(visited_array, adjacency_dict, node):
    if visited_array[node] == 1:
        return
    
    global traversal_order
    traversal_order.append(node)
    visited_array[node] = 1

    for neighbour in adjacency_dict[node]:
        if visited_array[neighbour] != 1:
            dfs_traverse(visited_array, adjacency_dict, neighbour)

    return

if __name__ == "__main__":
    n, m, starting_node = map(int, input().split())
    edges = []
    for i in range(m):
        node_from, node_to = map(int, input().split())
        edges.append([node_from, node_to])

    adj_list = create_adjacency_list(n, edges)
    visited_array = [0] * (n + 1)
    dfs_traverse(visited_array, adj_list, starting_node)
    
    print(traversal_order)


    