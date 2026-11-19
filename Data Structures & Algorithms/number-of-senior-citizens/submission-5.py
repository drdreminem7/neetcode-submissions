class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num = 0
        for detail in details:
            num += 1 if int(detail[11:13]) > 60 else 0
        return num