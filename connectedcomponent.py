from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(n1):
            res = n1

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res


sol = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(sol.countComponents(n, edges))
