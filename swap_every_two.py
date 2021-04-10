from sll import Node, construct_sll

def swap_every_two(head: Node) -> Node:
    curr = head
    while curr != None:
        next = curr.next
        if next != None:
            curr.next, next.next = next.next, curr.next
            next = 