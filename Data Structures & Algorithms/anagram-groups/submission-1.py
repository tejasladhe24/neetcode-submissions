class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = dict()

        for elem in strs:
            count = [0]*26

            for c in elem:
                count[ord(c)-ord("a")] += 1
            
            key = tuple(count)

            if key not in data:
                data[key] = []
            data[key].append(elem)

        return list(data.values())