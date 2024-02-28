class Solution:
    def reverseWords(self, s: str) -> str:
        j = len(s) - 1
        res = ""
        for i in range(len(s) - 1, -1, -1):
            temp=i
            while s[i] == " " and temp < j:
                temp+=1
                res += s[temp]
                if temp == j:
                    j = i-1
                    res += " "
        for i in range(j+1):
            res += s[i]
  
                
        res = re.sub(' +', ' ', res)
        return res.strip()