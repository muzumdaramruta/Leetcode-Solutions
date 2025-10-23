class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        graph = defaultdict(dict)
        
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
        
        # Step 2: DFS function
        def dfs(curr, target, visited):
            if curr not in graph or target not in graph:
                return -1.0
            if curr == target:
                return 1.0
            
            visited.add(curr)
            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0
        
        # Step 3: Process queries
        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))
        
        return results