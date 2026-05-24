class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)
        ans = [0] * (2 * len(nums))

        for i in nums:
            ans[l] = nums[l]
            ans[r] = nums[l]
            l += 1
            r += 1

        return ans