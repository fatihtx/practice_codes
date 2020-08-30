class Solution:
    def minTimeToVisitAllPoints(self, points):
        axesCX,axesCY = points[0]
        return_p = 0
        for axesNX,axesNY in points[1:]:
            return_p += max(abs(axesCX-axesNX), abs(axesCY-axesNY))
            axesCX,axesCY = axesNX,axesNY
        return return_p
