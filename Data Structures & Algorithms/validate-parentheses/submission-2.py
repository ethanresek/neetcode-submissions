class Solution:
    def isValid(self, s: str) -> bool:
        left_set = {'(', '{', '['}
        right_set = {')', '}', ']'}
        partners = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c in left_set:
                stack.append(c)
            elif c in right_set:
                if not stack or stack.pop() != partners[c]:
                    return False
            else:
                return False
        
        if stack:
            return False
        return True