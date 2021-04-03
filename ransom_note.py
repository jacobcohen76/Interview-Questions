import collections

from typing import List

def can_spell(magazine: List[str], word: str) -> bool:
    counter = collections.Counter(magazine)
    for letter in word:
        if counter[letter] > 0:
            counter[letter] -= 1
        else:
            return False
    return True

print(can_spell(['A', 'B', 'C', 'D', 'E', 'F'], 'BED'))
print(can_spell(['A', 'B', 'C', 'D', 'E', 'F'], 'CAT'))