class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        output = []
        for i in range(len(nums)):
            if target - nums[i] in store:
                output.append(store[target-nums[i]])
                output.append(i)
                return output
            else:
                store[nums[i]] = i
        