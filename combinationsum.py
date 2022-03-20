from typing import List

class Solution:
    def combinationSumOld(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(t, path, index):
            if t == 0:
                return path
            for i in range(index, len(candidates)):
                cur = candidates[i]
                if t >= cur:
                    cur_path = dfs(t-cur, path + [cur], i)
                    if cur_path:
                        res.append(cur_path)
                else:
                    return False
        
        dfs(target, [],0)
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return
            if i>=len(candidates) or target < total:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0,[],0)
        return res

sol = Solution()
cand = [2, 3, 6, 7]
target = 7
print(sol.combinationSum(cand, target))
