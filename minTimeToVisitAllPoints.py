class Solution:
    def minTimeToVisitAllPoints(self, points):
        return_p = 0
        for index,axes in enumerate(points):
            if index == 0:
                x1,y1 = axes
            else:
                [x2,y2] = axes
                xdiff = x1-x2
                ydiff = y1-y2
                mix_n = min(abs(xdiff),abs(ydiff))
                diffx = abs(xdiff) - mix_n
                diffy = abs(ydiff) - mix_n
                print (diffx + diffy)
                return_p += abs(diffx + diffy) + mix_n  
                x1,y1 = axes
        return return_p
