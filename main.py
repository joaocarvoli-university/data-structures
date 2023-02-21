import sys

sys.path.append("lists")

from lists import linked

lk = linked.LinkedList()
lk.append(2)
lk.append(3)

print(f'The size of the Linked list is: {len(lk)}')  # expected result: 2
print(lk[0])  # expected result: 2
print(lk[1])  # expected result: 3
lk[1] = 1
print(lk[1])  # expected result: 1
print(lk[2])  # expected result: error -> list index out of range
