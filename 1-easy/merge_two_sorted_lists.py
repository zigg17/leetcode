from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return None

        final_list_head = ListNode()
        final_list_iterator = final_list_head
        
        while list1 and list2:
            if list1.val <= list2.val:
                final_list_iterator.val = list1.val
                list1 = list1.next
            else:
                final_list_iterator.val = list2.val
                list2 = list2.next
            if list1 and list2:
                final_list_iterator.next = ListNode()
                final_list_iterator = final_list_iterator.next
            
        if list1 and not list2:
            final_list_iterator.next = list1
        if list2 and not list1:
            final_list_iterator.next = list2
            
        return final_list_head

# Function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test Case 1: Both lists are empty
list1 = None
list2 = None

solution = Solution()
result = solution.mergeTwoLists(list1, list2)
print("Test Case 1")
print(result)  # Expected: None

# Test Case 2: One list is empty
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = None

result = solution.mergeTwoLists(list1, list2)
print("Test Case 2")
print_list(result)  # Expected: 1 -> 2 -> 4 -> None

# Test Case 3: Both lists have elements, with no overlap in values
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

result = solution.mergeTwoLists(list1, list2)
print("Test Case 3")
print_list(result)  # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# Test Case 4: Lists have overlapping values
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

result = solution.mergeTwoLists(list1, list2)
print("Test Case 4")
print_list(result)  # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

# Test Case 5: One list is completely smaller than the other
list1 = ListNode(1, ListNode(1, ListNode(1)))
list2 = ListNode(2, ListNode(2, ListNode(2)))

result = solution.mergeTwoLists(list1, list2)
print("Test Case 5")
print_list(result)  # Expected: 1 -> 1 -> 1 -> 2 -> 2 -> 2 -> None

# Test Case 6: Both lists are identical
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(1, ListNode(2, ListNode(3)))

result = solution.mergeTwoLists(list1, list2)
print("Test Case 6")
print_list(result)  # Expected: 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> None