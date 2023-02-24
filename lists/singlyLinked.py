from nodes import SimpleNode


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def add_start(self, data: int):
        if self._head is None:
            node = SimpleNode(data)
            self._head = node
            self._tail = node
            self._size += 1
        else:
            node = SimpleNode(data)
            node.next = self._head
            self._head = node

    def add_end(self, data: int):
        if self._head is None:
            node = SimpleNode(data)
            self._head = node
            self._tail = node
            self._size += 1
        else:
            node = SimpleNode(data)
            if self._size == 1:
                self._head.next = node
                self._tail = node
            else:
                self._tail.next = node
                self._tail = node
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

    def get_head_data(self):
        return self._head.data

    def get_tail_data(self):
        return self._tail.data

    def print(self):
        print("#### PRINTING ELEMENTS ####")
        if self._head is None:
            print("There is no any element in the list")
        else:
            temp = self._head
            while temp.next:
                print(temp.data)
                temp = temp.next
            print(temp.data)
        print("#### FINISHING PRINT ####")
