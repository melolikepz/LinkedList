class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def insert_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_position(self, value, position):
        if position == 0:
            self.insert_begin(value)
        new_node = Node(value)
        current = self.head
        for node in (position - 1):
            current = current.next
        current.next = new_node
        self.size += 1

    def remove_end(self):
        if not self.head:
            return f"Empty"
        elif not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next and current.next.next:
                current = current.next

            current.next = None

    def remove_begin(self):
        if self.head == None:
            raise IndexError("List is empty")
        else:
            self.head = self.head.next
            self.size -= 1

    def remove_position(self, position):
        if position == 0:
            self.remove_begin()
        else:
            current = self.head
            for node in range(position - 1):
                current = current.next
            current.next = current.next.next
            self.size -= 1

    def get_size(self):
        return self.size

    def __getitem__(self, index):
        current = self.head
        for node in range(index - 1):
            current = current.next
        return current
