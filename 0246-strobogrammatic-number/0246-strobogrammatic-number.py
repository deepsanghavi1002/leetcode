class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strob = {'8':'8', '9':'6','6':'9','1':'1','0':'0'}
        rev = ""
        for i in num:
            if i in strob:
                rev = strob[i] + rev 
            else:
                return False
        print(rev,num)
        if rev == num:
            return True
        return False
