class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        
        this is shit complexity O(N^2) 

        adds all the chars from first string to a list

        iterates second string 

        if the char is in the list, remove it from the list

        if list length is 0 return true. 

        OH wait its not O(S+T) cus every time i iterate in T
        im checking all of S again in chars. fuck!

        '''

        if len(s) != len(t): return False

        chars = list(s)

        for char in t:
            if char in chars:
                chars.remove(char)

        if len(chars) == 0: return True

        return False