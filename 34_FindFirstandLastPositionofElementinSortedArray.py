from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find(isLeft):

            bound = -1

            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if isLeft:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return bound

        start = find(True)
        end = find(False)

        return [start, end]




