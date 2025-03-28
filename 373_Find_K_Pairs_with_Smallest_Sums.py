import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        heap = []

        for i in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[i], 0, i))

        while k > 0 and heap:
            cur_sum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            if i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return result





