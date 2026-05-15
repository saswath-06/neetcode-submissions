class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        out = []
        for i in nums:
            res[i] = res.get(i, 0) + 1
        
        res_sorted = sorted(res.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            out.append(res_sorted[i][0])

        return out

