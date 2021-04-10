from typing import Any, List

class Node:
    def __init__(self,
            val: Any,
            next: 'Node' = None
        ):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return '{name}@{id}(val={val})' \
            .format(
                name=self.__class__.__name__,
                id=id(self),
                val=self.val,
            )
    
    def __repr__(self) -> str:
        return self.__str__()

def construct_sll(vals: List[Any]) -> Node:
    nodes = [Node(val) for val in vals]
    for i in range(len(nodes)):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
    return nodes[0] if nodes else None
