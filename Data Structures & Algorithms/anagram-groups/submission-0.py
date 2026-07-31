class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for s in strs:
            s_default_list = [0]*26
            for c in s:
                s_default_list[ord(c)-ord("a")] += 1

            key = tuple(s_default_list)
            if key not in result_dict:
                result_dict[key] = []
            result_dict[key].append(s)
        
        print(list(result_dict.values()))
        return list(result_dict.values())


