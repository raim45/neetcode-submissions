class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for val in strs:
            key = tuple(sorted(val))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(val)

        return list(hashmap.values())