from node import DoublyNode


class DoublyLinkedList:
    def __init__(self, value):
        new_node = DoublyNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = DoublyNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = DoublyNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.length += 1
            return self.prepend(value)
        if index == self.length:
            self.length += 1
            return self.append(value)
        new_node = DoublyNode(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()
        target_index = self.get(index)
        target_index.prev.next = target_index.next
        target_index.next = None
        self.length -= 1
        return target_index

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = temp.prev
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
