class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if both sets are the same length, if they are not they cannot be an anagram
        if (len(s) != len(t)):
            return False
         #create a dictionary for both lists
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT