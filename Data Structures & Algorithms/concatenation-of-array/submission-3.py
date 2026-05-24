class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        r = len(nums)
        ans = [0] * (2 * r)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[r + i] = nums[i]

        return ans