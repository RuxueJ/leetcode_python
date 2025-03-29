from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, path = [], []

        def backtracking(startIndex, target):
            if target == 0:
                result.append(path[:])
                return

            if startIndex > len(candidates) - 1 or candidates[startIndex] > target:
                return

            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                target -= candidates[i]
                backtracking(i + 1, target)

                path.pop()
                target += candidates[i]

        backtracking(0, target)
        return result
