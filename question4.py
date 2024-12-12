#Ink
#1113536
#12/12/2024

class UnionFind:
   
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True

def minimum_spanning_tree_sum(V, edges):
 
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(V)
    mst_weight = 0
    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight

    return mst_weight

if __name__ == "__main__":
    # Test case 1: Example from homework problem
    V1 = 3
    edges1 = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
    result1 = minimum_spanning_tree_sum(V1, edges1)
    print("Test Case 1:", result1)

    # Test case 2: Another graph configuration
    V2 = 4
    edges2 = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
    result2 = minimum_spanning_tree_sum(V2, edges2)
    print("Test Case 2:", result2)
