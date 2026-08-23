class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # print(s,t)
        
        if len(s) != len(t):
            return False
        else:
            l1 = list(s.lower())
            l2 = list(t.lower())
            
            

str1 = "carIshere"
str2 = "hereiscar"

sol = Solution()
sol.isAnagram(str1,str2)