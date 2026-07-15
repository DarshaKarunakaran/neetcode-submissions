class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for st in strs:
            key = "".join(sorted(st))
            if key in seen:
                seen[key].append(st)
            else:
                seen[key] = [st]
        return list(seen.values())

        