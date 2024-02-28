class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i<j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
 
        
        i = 0
        j = 0
        while i < len(s):
            if s[i] == ' ':
                var = i - 1
                while j<var:
                    temp = s[var]
                    s[var] = s[j]
                    s[j] = temp
                    var -=1
                    j+=1
           
                i+=1
                j = i
            i+=1
            
  
        i-=1
        while i>j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j+=1
            i-=1
        print(s)