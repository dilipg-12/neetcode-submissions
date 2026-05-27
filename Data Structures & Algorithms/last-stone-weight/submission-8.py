class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones) == 1 : return stones[0]
        # weights = []
        # heapq.heapify(weights)
        # for s in stones:
        #     heapq.heappush(weights, -s)
        # while len(weights) > 1:
        #     j, i = -heapq.heappop(weights), -heapq.heappop(weights)
        #     value = j - i
        #     if value:
        #         heapq.heappush(weights, -value)
        # return -weights[0] if weights else 0
        # # return weights[0]
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])