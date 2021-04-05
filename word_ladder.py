import collections

from typing import Dict, Iterable, Set

def replace_letter(s: str, r: str, i: int) -> str:
    return s[:i] + r + s[(i + 1):]

def enumerate_word(word: str, letter: str):
    for i in range(len(word)):
        yield replace_letter(word, letter, i)

def make_adjacency(words: Iterable[str], letter: str) -> Dict[str, Set[str]]:
    adjacency = collections.defaultdict(set)
    for word in words:
        for key in enumerate_word(word, letter):
            adjacency[key].add(word)
    return adjacency

def bfs(words: Iterable[str], letter: str):
    
# print(replace(1, 'hot'))
