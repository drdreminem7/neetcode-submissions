class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0]
        for i in range(1, len(flowers) - 1):
            if not flowers[i - 1] and not flowers[i] and not flowers[i + 1]:
                flowers[i] = 1
                n -= 1
        return n <= 0