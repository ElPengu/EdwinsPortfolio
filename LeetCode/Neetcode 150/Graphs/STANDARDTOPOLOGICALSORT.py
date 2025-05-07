class Solution:

    def topological_sort_dfs(graph):
        visited = set()
        result = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            result.append(node)  # Post-order push

        for node in graph:
            if node not in visited:
                dfs(node)

        return result[::-1]  # Reverse for topological order

if __name__ == "__main__":
    sol = Solution
    graph = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        0: [],
        1: []
    }

    print(sol.topological_sort_dfs(graph)) # [4,5,0,2,3,1]
