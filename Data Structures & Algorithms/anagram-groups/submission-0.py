class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_pair = dict()
        for word in strs:
            key = "".join(sorted(word))
            sorted_pair.setdefault(key, []).append(word)
            
        return list(sorted_pair.values())
        