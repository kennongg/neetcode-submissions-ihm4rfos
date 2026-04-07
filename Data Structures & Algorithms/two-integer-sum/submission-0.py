class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums): # i = index, n = nums
            diff = target - n # target - val
            if diff in prevMap: # if the difference is in the map 
                return [prevMap[diff], i] # return the index
            prevMap[n] = i
        return
