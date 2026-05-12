class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap = {}
        # for val in strs:
        #     key = tuple(sorted(val))
        #     if key not in hashmap:
        #         hashmap[key] = []
        #     hashmap[key].append(val)

        # return list(hashmap.values())

        hashmap = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for ch in i:
                count[ord(ch) - ord("a")] += 1
            hashmap[tuple(count)].append(i)

        return list(hashmap.values())





