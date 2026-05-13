class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in num_dict:
                return [num_dict.get(difference), i]
            num_dict[n] = i