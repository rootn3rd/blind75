from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        
        adj = { i: [] for i in range(n) }
        for frm,to in edges:
            adj[frm].append(to)
            adj[to].append(frm)

        visit = set()
        def dfs(i, prev):
            if i in visit: return False

            visit.add(i)
            for nei in adj[i]:
                if nei == prev: continue
                if not dfs(nei, i): return False
            
            return True

        return dfs(0, -1) and len(visit) == n





sol = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(sol.valid_tree(n, edges))
