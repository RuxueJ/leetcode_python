class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        result = []
        path = []
        n = len(candidates)

        def backtracking(startIndex, current_sum):
            if current_sum == target:
                result.append(path[:])
                return
            if current_sum > target:
                return

            for i in range(startIndex, n):
                new_sum = current_sum + candidates[i]
                if new_sum > target:
                    break

                path.append(candidates[i])
                backtracking(i, new_sum)
                path.pop()

        backtracking(0, 0)
        return result

