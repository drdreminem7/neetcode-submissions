class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = Counter(arr1)
        hash_set = set(arr2)

        index = 0
        for num in arr2:
            count = hash_map[num]
            arr1[index : index + count] = [num] * count
            hash_map.pop(num)
            index += count

        for key, value in sorted(hash_map.items()):
            count = hash_map[key]
            arr1[index : index + count] = [key] * count
            index += count

        return arr1
