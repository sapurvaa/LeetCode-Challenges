'''
Check if a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: #check if only two points are given
            return True
        else:
            if coordinates[1][0]-coordinates[0][0] != 0:  #in case x-co-ordinates are same, parallel to y-axis, to avoid zero division error
                slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
                i=2
                while i<len(coordinates):
                    if coordinates[i][0]-coordinates[0][0]==0:  #points can't be parallel to y-axis, as that check was already done above
                        return False
                    else:
                        new_slope = (coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0])
                        if new_slope != slope:
                            return False
                    i=i+1
                return True
            else:   #checking for line parallel to y-axis whose slope is undefined
                i=1
                while i<len(coordinates):
                    if coordinates[i][0]!=coordinates[0][0]:
                        return False
                    i=i+1
                return True
