import collections

from bst import Node, construct_bst
from typing import Union

def is_valid_bst_recursive(head: Node) -> bool:
    def worker(node: Node, lower: Union[float, int], upper: Union[float, int]) -> bool:
        if node == None:
            return True
        elif lower < node.val and node.val < upper:
            return  worker(node.left,  lower, node.val) and \
                    worker(node.right, node.val, upper)
        else:
            return False
    return worker(head, float('-inf'), float('+inf'))

def is_valid_bst_iterative(head: Node) -> bool:
    stack = collections.deque([(head, float('-inf'), float('+inf'))])
    while stack:
        node, lower, upper = stack.pop()
        if node == None:
            continue
        elif lower < node.val and node.val < upper:
            stack.append((node.left,  lower, node.val))
            stack.append((node.right, node.val, upper))
        else:
            return False
    return True

head = construct_bst([5,1,4,None,None,3,6])
print(is_valid_bst_recursive(head))
print(is_valid_bst_iterative(head))
