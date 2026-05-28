class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = deque()
        counter = dict()
        for c in tasks:
            counter[c] = counter.get(c, 0) + 1
        heap = [-c for c in counter.values()]
        heapq.heapify(heap)
        print(heap)
        while heap or q:
            time += 1
            if heap:
                val = 1 + heapq.heappop(heap)
                if val:
                    q.append((val, time+n))
            
            if q and q[0][1] == time:
                val, t = q.popleft()
                heapq.heappush(heap, val)
        return time 
            