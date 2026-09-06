class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #approach: maybe use a duplicate list to store
        #as you store each number, check if it already exists in the temp list
        temp = set() #create an empty tests set 
        for i in nums: #iterate through nums
            if i in temp: #initially always false - check if i is in temp, return true if true 
                return True  
            temp.add(i) #adding i to temp
        return False #return false if no duplicates 