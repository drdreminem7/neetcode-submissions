class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] + asteroid == 0:
                    stack.pop()
                    break
                elif stack[-1] + asteroid > 0:
                    break
                else:
                    stack.pop()
            else: stack.append(asteroid)

        return stack