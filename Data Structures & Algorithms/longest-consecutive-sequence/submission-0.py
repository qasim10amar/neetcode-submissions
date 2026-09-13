class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_map = set(nums)
        max_length = 0

        
        for num in h_map:
            check = num
            if check - 1 in h_map:
                continue

            length = 1
            while num + length in h_map:
                length += 1


            max_length = max(max_length,length)

        return max_length