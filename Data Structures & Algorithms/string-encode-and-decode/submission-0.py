class Solution:
    
    def encode(self, strs: List[str]) -> str:
        trackingDict = {}
        i=0
        for ss in strs:
            trackingDict[i] = ss
            i = i+1
        import json
        s =  json.dumps(trackingDict)
        return s

    def decode(self, s: str) -> List[str]:
        import json
        converted_dict = json.loads(s)
        strList = []
        for k in converted_dict:
            strList.append(converted_dict[k])
        return strList