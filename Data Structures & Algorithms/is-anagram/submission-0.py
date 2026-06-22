class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        chars = list(s)

        for char in t:
            if char in chars:
                chars.remove(char)

        if len(chars) == 0: return True

        return False