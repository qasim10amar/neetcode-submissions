class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i in range (len(nums)):
            needed = target - nums[i]
            if needed in count:
                return[count[needed], i]
            count[nums[i]] = i
            
        
        
        
        
        # for z in range (len(nums)):
        #     for i in range (z + 1, len(nums)):
        #         if nums[z] + nums[i] == target:
        #             return [z,i]
                

