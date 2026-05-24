class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        r = len(nums)
        ans = [0] * (2 * r)

        for i, n in enumerate(nums):
            ans[i] = ans[r + i] = n

        return ans