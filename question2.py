#Ink
#1113536
#12/12/2024

from collections import deque

def bfs_traversal(adj):
   
    V = len(adj)
    visited = [False] * V
    bfs_order = []
    queue = deque([0])
    visited[0] = True

    while queue:
       
        curr = queue.popleft()
        bfs_order.append(curr)
      
        neighbors = sorted(adj[curr])
        for neighbor in neighbors:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return bfs_order

if __name__ == "__main__":
    # Test case 1: Example from homework problem
    adj1 = [[2,3,1], [0], [0,4], [0], [2]]
    result1 = bfs_traversal(adj1)
    print("Test Case 1:", result1)

    # Test case 2: Another graph configuration
    adj2 = [[1,2], [0,3], [0,3], [1,2]]
    result2 = bfs_traversal(adj2)
    print("Test Case 2:", result2)
