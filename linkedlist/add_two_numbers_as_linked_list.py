from sll import Node, construct_sll

def add_two_numbers_recursive(list1: Node, list2: Node) -> Node:
    def worker(list1: Node, list2: Node, carry: int) -> Node:
        if list1 == None and list2 == None:
            return Node(carry) if carry else None
        elif list1 != None:
            sum = list1.val + carry
            list3 = Node(sum % 10)
            list3.next = worker(list1.next, list2, sum // 10)
            return list3
        elif list2 != None:
            sum = list2.val + carry
            list3 = Node(sum % 10)
            list3.next = worker(list1, list2.next, sum // 10)
            return list3
        else:
            sum = list1.val + list2.val + carry
            list3 = Node(sum % 10)
            list3.next = worker(list1.next, list2.next, sum // 10)
            return list3
    return worker(list1, list2, 0)


