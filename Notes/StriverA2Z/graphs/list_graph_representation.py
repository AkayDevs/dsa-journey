from typing import List


# Can also be implemented using default dict
def create_adjacency_list(n : int, edges: List[List[int]]):
    adjacency_list = {}
    for i in range(1, n + 1):
        adjacency_list[i] = []
    
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append[u]
    
    return adjacency_list

if __name__ == "__main__":
    pass