class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            diff_r = target - numbers[l]
            diff_l = target - numbers[r]
            if numbers[r] + numbers[l] == target:
                return [l+1, r+1]
            if diff_r < numbers[r]:
                r -= 1
            if diff_l > numbers[l]:
                l += 1


        