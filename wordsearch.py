from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board)-1, len(board[0]) - 1
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r > ROWS or c > COLS or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            visited.remove((r, c))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False


sol = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(sol.exist(board, word))
