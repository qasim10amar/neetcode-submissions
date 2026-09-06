class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for z in range (len(nums)):
            for i in range (z + 1, len(nums)):
                if nums[z] + nums[i] == target:
                    return [z,i]
                
                
                
                # if num1 + num2 == target:
                #    i1 = nums.index(num1)
                #    i2 = nums.index(num2)
                #    return [i1,i2] 
