import collections

from typing import List

def sort_3_nums_swapping(nums: List[int]) -> None:
    def swap(i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
    i, one_ptr, three_ptr = 0, 0, len(nums) - 1
    while i <= three_ptr:
        if nums[i] == 1:
            swap(i, one_ptr)
            one_ptr += 1
            i += 1
        elif nums[i] == 2:
            i += 1
        elif nums[i] == 3:
            swap(i, three_ptr)
            three_ptr -= 1

def sort_nums_counting(nums: List[int], no_unique_nums: int) -> None:
    curr_index = 0
    counts = collections.Counter(nums)
    for i in range(no_unique_nums):
        num = min(counts.keys())
        for j in range(counts[num]):
            nums[curr_index] = num
            curr_index += 1
        del counts[num]

nums = [3, 3, 2, 1, 3, 2, 1]
sort_nums_counting(nums, 3)
print(nums)

nums = [3, 3, 2, 1, 3, 2, 1]
sort_3_nums_swapping(nums)
print(nums)