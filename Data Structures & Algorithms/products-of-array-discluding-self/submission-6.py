class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zerocount = 0
        res = []
        for i in nums:
            if i != 0:
             prod *= i
            if i==0:
                zerocount += 1
        
        for i, n in enumerate(nums):
            if zerocount >= 2:
                res.append(0)
            elif zerocount == 1:
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod//n)
        return res




            




        