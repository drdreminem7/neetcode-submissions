class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        for word in arr:
            if word in count and count[word] == 1:
                k -= 1
                del count[word]
                if k == 0:
                    return word
        return ""
        
