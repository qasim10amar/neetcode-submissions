class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1] 
        post_prod = [1] * len(nums)
        result = []

        for i in range(1, len(nums)):
            pre_prod.append(pre_prod[i-1] * nums[i-1])
        
        for i in range(len(nums) - 2, -1, -1):
            post_prod[i] = post_prod[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            result.append(pre_prod[i] * post_prod[i])
        
        return result