from typing import List

def create_adjacency_list(n : int, edges: List[List[int]]):
    adjacency_list = {}
    for i in range(1, n + 1):
        adjacency_list[i] = []
    
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    return adjacency_list

def dfs_traverse(visited_array, adjacency_list, node):
    if visited_array[node] == 1:
        return
    
    visited_array[node] = 1

    for neighbour in adjacency_list[node]:
        if visited_array[neighbour] != 1:
            dfs_traverse(visited_array, adjacency_list, neighbour)

    return

def get_number_of_provinces(n, adjacency_list):
    visited_array = [0] * (n + 1)

    province_count = 0
    for i in range(1, n + 1):
        if visited_array[i] != 1:
            province_count += 1
            dfs_traverse(visited_array, adjacency_list, i)

    return province_count
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        node_from, node_to = map(int, input().split())
        edges.append([node_from, node_to])

    adj_list = create_adjacency_list(n, edges)
    print(get_number_of_provinces(n, adj_list))