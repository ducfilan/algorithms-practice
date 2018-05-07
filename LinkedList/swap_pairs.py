# Given a linked list, swap every two adjacent nodes and return its head.
# 
# Example:
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:
# 
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swap_pairs(head):
    if not head or not head.next:
        return head
        
    start = head
    head = head.next
    nodes_group = []
    
    while start:
        nodes_group.append(start)
        start = start.next
        
        if len(nodes_group) == 4:
            nodes_group[1].next = nodes_group[0]
            nodes_group[0].next = nodes_group[3]
            start = nodes_group[2]
            nodes_group = []

	if len(nodes_group) == 3:
		nodes_group[1].next = nodes_group[0]
		nodes_group[0].next = nodes_group[2]
	else:
		nodes_group[1].next = nodes_group[0]
		nodes_group[0].next = None
        
    return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
node10 = ListNode(10)
node11 = ListNode(11)
node12 = ListNode(12)
node13 = ListNode(13)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12
node12.next = node13

go = node1

while go.next:
    print(go.val)
    go = go.next
else:
    print(go.val)

print("__________\n")

go = swap_pairs(node1)

while go.next:
    print(go.val)
    go = go.next
else:
    print(go.val)
