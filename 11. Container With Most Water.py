# 11. Container With Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Assign left pointer to the very left
        # and right pointer to the very right
        l, r = 0, len(height) - 1
        # store the result of the area (length x width)
        # we initialize result to 0 as an area can't be negative
        res = 0
        
        # left pointer can only by less than right pointer
        while l < r:
            # store the highest result of the previous result value
            # to the current result value
            res = max(res, min(height[l], height[r]) * (r - l))
            # if the height of the left pointer is less than the
            # height of the right pointer, we move the left pointer 
            # up one position
            if height[l] < height[r]:
                l += 1
            # else, we move the right pointer to the next position
            elif height[r] <= height[l]:
                r -= 1
         
        # we return the max area
        return res
