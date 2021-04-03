from typing import Any, List

class Node:
    def __init__(self,
            val: Any,
            left: 'Node' = None,
            right: 'Node' = None,
        ):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return '{name}@{id}(val={val})' \
            .format(
                name=self.__class__.__name__,
                id=id(self),
                val=self.val,
            )
    
    def __repr__(self) -> str:
        return self.__str__()

def construct_bst(vals: List[Any]) -> Node:
    def left(index: int) -> int:
        return 2 * index + 1
    def right(index: int) -> int:
        return 2 * index + 2
    nodes = [Node(val) if val != None else None for val in vals]
    for i in range(len(nodes)):
        if left(i) < len(nodes):
            nodes[i].left = nodes[left(i)]
        if right(i) < len(nodes):
            nodes[i].right = nodes[right(i)]
    return nodes[0] if nodes else None
