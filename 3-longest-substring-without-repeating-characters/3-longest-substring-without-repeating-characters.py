class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
          return 0 
        maxlen = 0
        currlen = 0
        n = len(s)
        pos = {}
        pos[s[0]] = 0
        st = 0
        start = 0
        t = 0
        for i in range(1,n):
            if s[i] not in pos:
                pos[s[i]] = i
            else:
                if pos[s[i]] >= st:
                    currlen = i - st

                    if currlen > maxlen:
                        maxlen = currlen
                        start = st
                    st = pos[s[i]] + 1
                pos[s[i]] = i
        
        if n - st > maxlen:
          maxlen = n - st
          start = st
        print(s[start:start+maxlen])
        return(maxlen)