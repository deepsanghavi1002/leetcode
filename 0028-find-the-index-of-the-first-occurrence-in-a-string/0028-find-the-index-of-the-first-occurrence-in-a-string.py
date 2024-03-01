class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
            
        for i in range(0, len(haystack) - len(needle)+1):
            print(i)
            if haystack[i] == needle[0]:
                print(haystack[i], "start macthing")
                haystackPtr = i
                for j in range(len(needle)):
                    if haystack[haystackPtr +j ] != needle[j]:
                        break
                    elif j == len(needle) - 1:
                            return haystackPtr
        return -1
            
