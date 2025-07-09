class Solution:

    def dfs(self, graph: dict, node: str):
        
        
        pass


if __name__ == "__main__":
    sol = Solution
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    #print("BFS starting from A:", bfs(graph, 'A'))  # Expected: ['A', 'B', 'C', 'D', 'E', 'F']
    print("DFS starting from A:", sol.dfs(graph, 'A'))  # Expected: ['A', 'B', 'D', 'E', 'C', 'F']