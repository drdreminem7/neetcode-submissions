class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        queue = deque()
        queue.append(("0000", 0))
        seen = set(deadends)

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
            return res

        while queue:
            lock, turns = queue.popleft()
            if lock == target: 
                return turns

            for child in children(lock):
                if child not in seen:
                    queue.append((child, turns + 1))
                    seen.add(child)

        return -1
            