class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_k_group(head, k):
    current = head
    count = 0
    prev = None
    next_node = None

    temp = current
    while temp and count < k:
        temp = temp.next
        count += 1

    if count == k:
        while current and count > 0:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count -= 1

        if next_node is not None:
            head.next = reverse_k_group(next_node, k)
    else:
        return head
    return prev

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

lt = [1, 2, 3, 4, 5]
k = 3
dummy = Node(0)
current = dummy
for num in lt:
    current.next = Node(num)
    current = current.next

print("Original List:")
print_linked_list(dummy.next)

result = reverse_k_group(dummy.next, k)
print(f"Reversed List in groups of {k}:")
print_linked_list(result)
