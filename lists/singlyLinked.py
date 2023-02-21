from nodes import SimpleNode


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def append(self, data: int):
        if self._head is None:
            node = SimpleNode(data)
            self._head = node
            self._size += 1
        else:
            temp = self._head
            while temp.next:
                temp = temp.next
            node = SimpleNode(data)
            temp.next = node
            self._size += 1

    def get(self, index):
        temp = self._head
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                raise IndexError("list index out of range")
        if temp:
            return temp.data
        else:
            raise IndexError("list index out of range")

    def set(self, index, value):
        temp = self._head
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                raise IndexError("list index out of range")
        if temp:
            temp.data = value
        else:
            raise IndexError("list index out of range")

    def search(self, elem):
        if self._head.data is elem:
            return f'The element {elem} was found!'
        else:
            temp = self._head
            while temp.next:
                if temp.data is elem:
                    return f'The element {elem} was found!'
                else:
                    temp = temp.next

            if temp.data is elem:
                return f"The element {elem} was found!"
            else:
                return f"The element {elem} wasn't found!"

    def size(self):
        return self._size
