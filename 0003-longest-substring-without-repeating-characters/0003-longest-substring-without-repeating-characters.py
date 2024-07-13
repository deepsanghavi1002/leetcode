class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        lastOccurence = {i:-1 for i in s}
         
        
        start = 0
        
        curr_len = 0
        max_len = 0
        
        
        
        for i in range(len(s)):
            
            char = s[i]
            
            
            if lastOccurence[char] >= start:
                start = lastOccurence[char] + 1
                
                
            
        
            lastOccurence[char] = i
        
        
            curr_len = i - start+ 1
            max_len = max(curr_len, max_len)
        return max_len
        
        
        