class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            num = [0]*26
            for c in s:
                num[ord(c) - ord("a")] += 1
            group[tuple(num)].append(s)
        
        return list(group.values())
    