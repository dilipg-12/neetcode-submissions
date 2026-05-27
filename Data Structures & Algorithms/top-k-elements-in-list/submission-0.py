class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)
        return sorted(count.keys(), key=lambda j: count[j], reverse=True)[:k]
        