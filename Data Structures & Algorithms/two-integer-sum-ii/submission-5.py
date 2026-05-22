class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        cursum = 0

        while l < r:
            cursum = numbers[r] + numbers[l]
            if cursum == target:
                return [l+1, r+1]
            if cursum > target:
                r -= 1
            if cursum < target:
                l += 1


        