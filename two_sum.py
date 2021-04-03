from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    found = dict()
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in found:
            return (i, found[complement])
        else:
            found[nums[i]] = i
    return None

print(two_sum([2,7,11,15], 18))
    