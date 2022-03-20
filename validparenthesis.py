class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        return len(stack) == 0

sol = Solution()
inp = "()()(){}[]"
print(sol.isValid(inp))
            