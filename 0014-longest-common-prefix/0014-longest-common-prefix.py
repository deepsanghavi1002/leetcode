def helper(s1,s2):
  i = 0
  j = 0
  n1 = len(s1)
  n2 = len(s2)
  result = ''
  while(i<n1 and j<n2):
    if(s1[i] != s2[j]):
      break

    result += s1[i]
    i+=1
    j+=1
  return(result)
class Solution:


      
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs
        if(len(strs) == 0):
            return('')
        if(len(strs) == 1):
            return(strs[0])
        p = helper(s[0],s[1])
        for i in range(2,len(s)):
            p = helper(p, s[i])
        return(p)