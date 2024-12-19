class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'(', '[', '{'}
        opening = []
        for char in s:
            if char in brackets:
                opening.append(char)
            else:
                if opening and 0 < ord(char) - ord(opening[-1]) < 3:
                    opening.pop()
                else:
                    return False
        if opening:
            return False
        return True

print(Solution().isValid("({{{{}}}))"))
