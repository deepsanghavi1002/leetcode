class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = defaultdict(int)
        i = 0
        j = 0
        maxRes = 0
        while i<=j and j< len(s):
            count[s[j]] += 1
           
            while len(count) > k:
                
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i+= 1
                
            maxRes = max(j-i+1,maxRes)
            j+=1
                
        return maxRes
                
                
                
            
        
        
            
        