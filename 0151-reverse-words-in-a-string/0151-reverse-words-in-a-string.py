class Solution:
    def reverseWords(self, s: str) -> str:
        j = len(s) - 1
        res = ""
        spaceIndex = -1
        wordAppend = False
        for i in range(len(s) - 1, -1, -1):
            temp=i
            if (s[i] == " ") and (spaceIndex == i + 1):
                spaceIndex -= 1
                continue
            if spaceIndex != -1:
                j = spaceIndex - 1
            while s[i] == " " and temp < j:
                spaceIndex = i
                temp+=1
                res += s[temp]
                wordAppend = True
            if wordAppend:
                res += " "
                wordAppend = False
            
                
            
            
              
        """   
          print(res, temp, j)
                if temp == j:
                    j = i-1
                    res += " "
        """      
        if s[i] != " ":
            for i in range(j+1):
                res += s[i]
  
        return(res.strip())