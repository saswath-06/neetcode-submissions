class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        frequency = dict(sorted(frequency.items(), key=lambda item: item[1]))
        frequency = list(frequency.items())
        arr = []
        for i in range(k):
            arr.append(frequency[-(k-i)][0])
        return arr