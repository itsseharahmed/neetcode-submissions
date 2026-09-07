class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        temp = {} #temporary dict to hold numbers and indices
        for i, num in enumerate(nums): #check numbers and indices
            difference = target - num  #find difference of current number from target 
            if difference in temp: #if difference exists in temp
                return [temp[difference],i] #return difference and current number indices
            temp[num] = i # add current number and index to temp 
        return []      