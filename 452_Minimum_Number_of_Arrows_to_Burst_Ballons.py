class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key=lambda x: x[1])

        arrow_place = points[0][1]
        arrow_count = 1

        for point in points:
            if point[0] > arrow_place:
                arrow_count += 1
                arrow_place = point[1]

        return arrow_count
