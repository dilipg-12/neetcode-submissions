class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points.sort(key=lambda p: p[0]**2 + p[1]**2)
        # return points[:k]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        distance = []
        for i,j in points:
            distance.append([i**2+j**2, i, j])
        heapq.heapify(distance)

        res = []
        while k > 0:
            dis, i, j = heapq.heappop(distance)
            res.append([i, j])
            k-= 1
        return res


        