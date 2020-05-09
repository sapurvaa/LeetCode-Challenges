'''
Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        else:
            if coordinates[1][0]-coordinates[0][0] != 0:
                slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
                i=2
                while i<len(coordinates):
                    if coordinates[i][0]-coordinates[0][0]==0:
                        return False
                    else:
                        new_slope = (coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0])
                        if new_slope != slope:
                            return False
                    i=i+1
                return True
            else:
                i=1
                while i<len(coordinates):
                    if coordinates[i][0]!=coordinates[0][0]:
                        return False
                    i=i+1
                return True