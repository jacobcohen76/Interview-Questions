from typing import List

def min_jumps(nums: List[int]) -> int:
    table = [float('inf')] * len(nums)
    table[0] = 0
    for i in range(len(nums)):
        for step in range(i + 1, min(nums[i] + i + 1, len(nums))):
            table[step] = min(table[step], table[i] + 1)
    return table[-1]

print(min_jumps([3, 2, 5, 1, 1, 9, 3, 4]))
