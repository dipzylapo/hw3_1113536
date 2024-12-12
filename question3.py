#Ink
#1113536
#12/12/2024

def dfs_traversal(adj):

    V = len(adj)
    visited = [False] * V
    dfs_order = []

    def dfs_recursive(vertex):
      
        visited[vertex] = True
        dfs_order.append(vertex)
        neighbors = sorted(adj[vertex])
        for neighbor in neighbors:
            if not visited[neighbor]:
                dfs_recursive(neighbor)

    dfs_recursive(0)

    return dfs_order

if __name__ == "__main__":
    # Test case 1: Example from homework problem
    adj1 = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
    result1 = dfs_traversal(adj1)
    print("Test Case 1:", result1)

    # Test case 2: Another graph configuration
    adj2 = [[1,2], [0,3], [0,3], [1,2]]
    result2 = dfs_traversal(adj2)
    print("Test Case 2:", result2)
