class Solution:
    def isValid(self, s: str) -> bool:
        """
        s only has ()[]{}
        solution is to have a stack that keeps count of all open parantheses.
        every time we loop over a closing paranthese, we check if the top of the stack
        holds the corresponding opening paranthese

        time: O(n)
        space: O(n)
        """

        open_brackets = ["[", "(", "{"]
        corr_brackets = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        stack = []

        for x in s:
            if x in open_brackets:
                stack.append(x)

            else:
                if stack and stack[-1] == corr_brackets[x]:
                    stack.pop()
                else:
                    return False

        # we only return True if stack is empty (all brackets close)
        return False if stack else True