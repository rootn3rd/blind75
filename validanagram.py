class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countMap = {}
        
        for c in s:
            if c in countMap:
                countMap[c] +=1
            else:
                countMap[c] =1 
        
        for c in t:
            if c not in countMap:
                return False
            countMap[c] -=1
        
        for v in countMap.values():
            if v != 0:
                return False
        return True