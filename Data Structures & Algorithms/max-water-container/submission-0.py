class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        height_count = {}

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            height_count[area] = height_count.get(area, 0) + 1

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return max(height_count)