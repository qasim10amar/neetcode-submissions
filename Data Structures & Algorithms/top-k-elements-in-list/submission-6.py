class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # hmap = defaultdict(list)
        # # for 
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # sort = []
        # for key, values in count.items():
        #     sort.append([values,key])
        # sort.sort()
  
        # arr = []
        # while(len(arr) < k):
        #     arr.append(sort.pop()[1])
        # return arr
        hmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)

        for key, value in hmap.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
