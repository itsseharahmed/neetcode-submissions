from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         #count frequencies and grab the k most common
        frequency_map = Counter(nums)
        
        #most_common(k) returns a list of tuples: [(element, frequency)]
        #extract elements from tuple
        return [item[0] for item in frequency_map.most_common(k)]
