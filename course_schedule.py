import collections

from typing import Dict, List, Set, Tuple

def course_schedule(no_courses: int, prereqs: List[Tuple[int, int]]) -> bool:
    def construct_adjacency(prereqs: List[Tuple[int, int]]) -> Dict[Set[int]]:
        adjacency = collections.defaultdict(set)
        for course, prereq in prereqs:
            adjacency[course].add(prereq)
        return adjacency
    adjacency = construct_adjacency(prereqs)
    for course in range(no_courses):
        for prereq in adjacency[course]:
            if course in adjacency[prereq]:
                return False
    return True


