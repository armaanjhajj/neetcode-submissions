class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        this is the neetcode sol using hash sets
        '''

        if len (s) != len (t): return False

        countS = {} ## declaring hash sets
        countT = {}

        for i in range(len(s)):
            
            ## the key for count set is the letter/char 
            ## refd by index i of s

            ## if i did just add 1 to itself, the key/val could not exist
            ## so use get function with default param set to 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t [i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0): 
                return False

        return True 





