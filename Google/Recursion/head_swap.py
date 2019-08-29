"""
Auhtor: Emily Costa
Created on: 8/28/2019
Swaps every two adjacent nodes and returns its head for a linked list.
"""

def swap(head):
    # first, swap the first two nodes in the list (head and head.next)
    tempHead = head
    head = head.next
    head.next = tempHead

    swap(head.next.next)

    return head

if __name__=="__main__":
    # test
