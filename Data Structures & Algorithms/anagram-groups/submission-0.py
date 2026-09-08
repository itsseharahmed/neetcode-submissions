from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash map that creates empty list for new keys 
        anagrams = defaultdict(list)
        for ch in strs:
            #sort characters 
            sorted_word = "".join(sorted(ch))
            # add original string to corresponding list
            anagrams[sorted_word].append(ch)
        return list(anagrams.values())
            