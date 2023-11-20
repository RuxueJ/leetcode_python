class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # my_dict = defaultdict(list)
        # result = []
        # for i in range(len(nums)):
        #     my_dict[nums[i]].append(i)

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         target = -nums[i]-nums[j]
        #         if ((target in my_dict)):
        #             for k in my_dict[target]:
        #                 if (k != i and k !=j):
        #                     triplet = sorted([nums[i],nums[j],nums[k]])
        #                     if triplet not in result:
        #                         result.append(triplet)
        # return result

        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            # erase duplicated i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ > 0:
                    k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # new k
                    k -= 1
                    # new j
                    j -= 1

        return result


