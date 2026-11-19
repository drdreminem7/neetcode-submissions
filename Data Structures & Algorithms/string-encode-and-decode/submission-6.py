class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""

        result, sizes = "", []
        for s in strs: sizes.append(len(s))
        for size in sizes:
            result += str(size)
            result += ","
        result += "#"
        result += "".join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        if not s: return []

        strs, sizes, i = [], [], 0
        while s[i] != "#":
            j = i
            while s[j] != ",": j += 1
            sizes.append(int(s[i:j]))
            i = j + 1

        i += 1
        for size in sizes:
            strs.append(s[i:i+size])
            i += size

        return strs 