#Ink
#1113536
#12/12/2024

def create_adjacency_list(V, edges):

    adj_list = [[] for _ in range(V)]
    for u, v in edges:
        # Add v to u's list
        adj_list[u].append(v)
        # Add u to v's list (since it's an undirected graph)
        adj_list[v].append(u)

    for i in range(V):
        adj_list[i].sort()

    return adj_list

if __name__ == "__main__":
    # Test case 1: Example from homework problem
    V1 = 5
    edges1 = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
    result1 = create_adjacency_list(V1, edges1)
    print("Test Case 1:", result1)

    # Test case 2: Another graph configuration
    V2 = 4
    edges2 = [[0,1], [0,2], [1,3], [2,3]]
    result2 = create_adjacency_list(V2, edges2)
    print("Test Case 2:", result2)
