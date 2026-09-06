class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            numOfChars = [0] * 26
            for char in word:
                numOfChars[ord(char) - ord("a")] +=1
            if tuple(numOfChars) in hmap:
                hmap[tuple(numOfChars)].append(word)
            else:
                hmap[tuple(numOfChars)] = []
                hmap[tuple(numOfChars)].append(word)
        
        return list(hmap.values())
        