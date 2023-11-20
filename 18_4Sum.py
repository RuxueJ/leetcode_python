class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        length = len(nums)
        result = []

        for a in range(length):

            # not while loop
            if nums[a] > target and target >= 0 and nums[a] >= 0:
                break

            if a > 0 and nums[a] == nums[a - 1]:
                continue

            sum3 = target - nums[a]
            for b in range(a + 1, length):

                # not while loop
                if nums[b] > sum3 and sum3 > 0:
                    break

                # erase duplicate b
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c = b + 1
                d = length - 1
                while c < d:
                    if nums[b] + nums[c] + nums[d] > sum3:
                        d -= 1
                    elif nums[b] + nums[c] + nums[d] < sum3:
                        c += 1
                    else:
                        result.append([nums[a], nums[b], nums[c], nums[d]])

                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
        return result

