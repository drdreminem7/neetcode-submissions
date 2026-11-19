from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        S, T = len(s), len(t)
        if S < T: return ""

        t_chars = defaultdict(int)
        for i in range(T): t_chars[t[i]] += 1

        window_chars = defaultdict(int)
        min_w = 10**6
        start_index = -1

        have = 0
        need = len(t_chars)

        l = 0
        for r in range(S):
            window_chars[s[r]] += 1
            if s[r] in t_chars and window_chars[s[r]] == t_chars[s[r]]: have += 1
            while have == need:
                w = r - l + 1
                if w < min_w: 
                    start_index = l
                    min_w = w
                
                if s[l] in t_chars and window_chars[s[l]] == t_chars[s[l]]:
                    have -= 1

                if window_chars[s[l]] == 1: del window_chars[s[l]]
                else: window_chars[s[l]] -= 1

                l += 1

        if min_w == 10**6: return ""
        else: return s[start_index: start_index + min_w]