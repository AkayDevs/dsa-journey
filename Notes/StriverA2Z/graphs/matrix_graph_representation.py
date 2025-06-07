from typing import List

def create_adjacency_matrix(n: int, edges: List[List[int]]):
    adjacency_matrix = [[0] * n for _ in range(n)]

    for edge in edges:
        u, v = edge
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1

    return adjacency_matrix


if __name__ == "__main__":
    n = 3
    edges1 = [(0, 1), (1, 2), (2, 0)]
    adj_matrix1 = create_adjacency_matrix(n, edges1)
    for row in adj_matrix1:
        print(row)