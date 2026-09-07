from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #clean strings   
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()

        #check for equal length
        if len(s) != len(t):
            return False
    
        #use Counter to check frquency map 
        return Counter(s) == Counter(t)

