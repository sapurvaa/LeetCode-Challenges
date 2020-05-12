'''
Problem:

 An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image. 

Example 1:

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''

class Solution:
    def colour(self, sr, sc, newColour, image, oldColour):
        r=len(image)
        c=len(image[0])
        image[sr][sc] = newColour
        while (-1<(sr-1)<r) and (-1<sc<c) and image[sr-1][sc] == oldColour:
            image = self.colour(sr-1, sc, newColour, image, oldColour)
        while (-1<(sr+1)<r) and (-1<sc<c) and image[sr+1][sc] == oldColour:
            image = self.colour(sr+1, sc, newColour, image, oldColour)
        while (-1<sr<r) and (-1<(sc-1)<c) and image[sr][sc-1] == oldColour:
            image = self.colour(sr, sc-1, newColour, image, oldColour)
        while (-1<sr<r) and (-1<(sc+1)<c) and image[sr][sc+1] == oldColour:
            image = self.colour(sr, sc+1, newColour, image, oldColour)
        return image

    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        if image[sr][sc] == newColor:
            return image
        else:
            oldColour = image[sr][sc]
            new_image = self.colour(sr, sc, newColor, image, oldColour)
            return new_image

s=Solution()
im = s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
print(im)



