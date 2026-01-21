from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # e.g., nums = [1,2,1,2,1,2,3,1,3,2]
        # freq looks like:
        # Counter({1: 4, 2: 4, 3: 2})
        # so freq stored: {num1: count1, num2: count2, ...}
        freq = Counter(nums)
        print(freq)

        heap = [] # this stores a list of (count, num)
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for count, num in heap:
            result.append(num)
        return result

sol = Solution()
nums = [1,2,1,2,1,2,3,1,3,2]
print(sol.topKFrequent(nums, 2))
