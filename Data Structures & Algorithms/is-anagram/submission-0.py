class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        countArray = [0] * 26

        for i in range(len(s)):
            countArray[ord(s[i]) - ord('a')] += 1
            countArray[ord(t[i]) - ord('a')] -= 1

        # return all(c == 0 for c in countArray)

        for c in countArray:
            if (c != 0):
                return False
            
        return True