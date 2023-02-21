import sys

sys.path.append("lists")

from lists import singlyLinked

lk = singlyLinked.SinglyLinkedList()
lk.append(2)
lk.append(3)

print(lk.search(3))  # expected result: The element 3 was found!
print(lk.search(4))  # expected result: The element 4 wasn't found!
print(lk.search(2))  # expected result: The element 2 was found!

print(f'The size of the Linked list is: {lk.size()}')  # expected result: 2
print(lk.get(0))  # expected result: 2
print(lk.get(1))  # expected result: 3
lk.set(1, 1)
print(lk.get(1))  # expected result: 1
print(lk.get(2))  # expected result: error -> list index out of range
