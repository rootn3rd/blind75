from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) -1

        while l<r:
            for i in range(r - l):
                top, bottom = l, r

                topleft = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]

                matrix[bottom-i][l] = matrix[bottom][r-i]

                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topleft
            l+=1
            r-=1

sol = Solution()
arr = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(arr)
print(arr)