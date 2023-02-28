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
        else:
            node = SimpleNode(data)
            node.next = self._head
            self._head = node
            self._tail = node
        self._size += 1

    def add_at(self, data: int, position: int):
        if self._head is None:
            node = SimpleNode(data)
            self._head = node
            self._tail = node
            self._size += 1
        else:
            counter = 0
            previous_node = self._head
            actual_node = self._head
            node = SimpleNode(data)

            if actual_node.next:
                while actual_node.next and counter <= position:
                    if counter > 0:
                        previous_node = actual_node

                    actual_node = actual_node.next
                    counter += 1

                previous_node.next = node
                node.next = actual_node
                self._tail = actual_node
            else:
                if position == 0:
                    self._head = node
                    node.next = previous_node
                    self._tail = previous_node
                else:
                    previous_node.next = node
                    self._tail = node
        self._size += 1

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

    def remove_first_occurrence(self, data):
        if self._head is None:
            return "This element doesn't exists"
        else:
            element_found = False
            counter = 0
            previous_node = self._head
            actual_node = self._head
            while actual_node.next:
                if counter > 0:
                    previous_node = actual_node
                if actual_node.data == data:
                    element_found = True
                    actual_node = actual_node.next
                    break

            if element_found:
                if actual_node:
                    previous_node.next = actual_node.next
                elif actual_node.next is None:
                    previous_node = None
                del actual_node
                return "Element removed"
            else:
                return "Element not found"

    def get(self, index) -> int:
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

    def search(self, elem) -> str:
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

    def size(self) -> int:
        return self._size

    def get_head_data(self) -> int:
        return self._head.data

    def get_tail_data(self) -> int:
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
