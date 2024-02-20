class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        currMax = 0
        globalMax = 0
        s =s.strip(" ")
        for i in range(len(s)):
            if s[i] != " ":
                currMax +=1
            else:
                currMax = 0
                
            globalMax = max(currMax, globalMax)
        return currMax