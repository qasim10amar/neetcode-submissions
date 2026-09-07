class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hmap = defaultdict(list)
        # for 
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sort = []
        for key, values in count.items():
            sort.append([values,key])
        sort.sort()
  
        arr = []
        while(len(arr) < k):
            arr.append(sort.pop()[1])
        return arr