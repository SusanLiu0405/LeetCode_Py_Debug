import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            while len(heap) > k:
                heappop(heap)
        return heap[0]

sol = Solution()


