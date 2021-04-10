from typing import List, Tuple

def get_ranges(nums: List[int], target: int) -> Tuple[int, int]:
    def binary_search_first(nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            if (mid == 0 or target > nums[mid - 1]) and nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lower = mid + 1
            else:
                upper = mid - 1
        return -1
    def binary_search_last(nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            if (mid == len(nums) - 1 or target < nums[mid + 1]) and nums[mid] == target:
                return mid
            elif target < nums[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
        return -1
    return (binary_search_first(nums, target), binary_search_last(nums, target))

print(get_ranges([1,3,3,5,7,8,9,9,9,15], 9))

