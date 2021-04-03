import collections
import functools
import operator

from typing import List

def find_non_duplicate_map(nums: List[int]) -> int:
    counter = collections.Counter(nums)
    for key in counter:
        if counter[key] == 1:
            return key
    return None

def find_non_duplicate_xor(nums: List[int]) -> int:
    return functools.reduce(operator.xor, nums)

print(find_non_duplicate_map([4,3,2,4,1,3,2]))
print(find_non_duplicate_xor([4,3,2,4,1,3,2]))