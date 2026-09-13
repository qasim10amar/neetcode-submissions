class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post_prod = [1] * len(nums)
        pre_prod = [1] * len(nums)


        for i in range(len(nums) - 2, -1, -1):
            post_prod[i] = nums[i+1] * post_prod[i+1]

        for i in range(len(nums) - 1):
            pre_prod[i+1] = pre_prod[i] * nums[i]

        result = []
        for i in range(len(nums)):
            total = pre_prod[i] * post_prod[i]
            result.append(total)
        
        return result


