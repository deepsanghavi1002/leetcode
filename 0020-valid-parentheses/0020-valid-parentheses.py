class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in ["(","{","["]:
                stk.append(i)
            
            if i in [")","}","]"]:
                if len(stk) == 0:
                    return False
                elem = stk.pop()
                if (i == ")" and elem != "(") or (i == "]" and elem != "[") or (i == "}" and elem != "{"):
                    return False
        return True if len(stk) == 0 else False
     
      