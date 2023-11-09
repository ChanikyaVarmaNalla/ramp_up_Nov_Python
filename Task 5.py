class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse_k_group(self, head, k):
        current = head
        count = 0

        while current and count < k:
            current = current.next
            count += 1

        if count == k:
            current = self.reverse_k_group(current, k)
            while count > 0:
                temp = head.next
                head.next = current
                current = head
                head = temp
                count -= 1
            head = current
        return head

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    linked_list.append(number)
print("Original Linked List:")
linked_list.traverse()

kth = 2
linked_list.head = linked_list.reverse_k_group(linked_list.head, kth)
print(f"\nReversed Linked List in groups of {kth}:")
linked_list.traverse()
