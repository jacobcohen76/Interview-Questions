from sll import Node, construct_sll

def reverse_sll(head: Node) -> Node:
    prev, curr = None, head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
    return prev

head = construct_sll([1,2,3,4,5])
head = reverse_sll(head)

curr = head
while curr != None:
    print(curr)
    curr = curr.next