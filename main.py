import sys

sys.path.append("tests")

from tests import singlyLinkedList

singlyLinkedList



#lk = singlyLinked.SinglyLinkedList()
#lk.add_start(10)
#
#lk.add_at(5, 1)
#
#lk.print()  # List: [10, 5]
#
#lk.add_start(11)
#
#lk.print()  # List: [11, 10, 5]
#
#lk.add_at(7, 2)
#
#lk.print()  # List: [11, 10, 7, 5]
#
#print(lk.get(0))  # expected result: 11
#
#lk.add_end(2)
#lk.add_end(4)
#lk.add_end(3)
#
#lk.print()  # List: [11, 10, 7, 5, 2, 4, 3]
#
#print(lk.get(1))  # expected result: 10
#print(lk.get(2))  # expected result: 7
#
#print(lk.search(3))  # expected result: The element 3 was found!
#print(lk.search(8))  # expected result: The element 8 wasn't found!
#print(lk.search(2))  # expected result: The element 2 was found!
#
#print(f'The size of the list is: {lk.size()}')  # expected result: 7
#print(f'The head of the list is: {lk.get_head_data()}')  # expected result: 11
#print(f'The tail of the list is: {lk.get_tail_data()}')  # expected result: 3
#
#print(f"Trying to remove number 1: {lk.remove_first_occurrence(5)}")
#lk.print()
#
##print(lk.get(8))  # expected result: error -> list index out of range
#