import collections

from typing import List

def multitasking(jobs: List[int], cooldown: int) -> int:
    counter = collections.Counter(jobs)
    for key in counter.keys():
        