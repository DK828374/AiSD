from typing import Any


class Node:
    def __init__(self, value=Any):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def node(self, at: int) -> None:
        node = self.head
        if self.head is not Node:
            for x in range(at):
                node = node.next
            return node
        raise ValueError("lista jest pusta")

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        node.next = after.next
        after.next = node

    def pop(self) -> Any:
        if self.head is not None:
            current = self.head
            self.head = current.next
            return current.value
        raise ValueError("lista jest pusta")

    def remove_last(self) -> Any:
        node1 = self.head
        node2 = self.head
        if self.head is not None:
            if self.head.next is not None:
                while node1.next is not None:
                    node1 = node1.next
                while node2.next is not node1:
                    node2 = node2.next
                last = node1
                node2.next = None
                return last.value
            last = self.head
            self.head = None
            return last.value
        raise ValueError("lista jest pusta")

    def remove(self, after: Node) -> Any:
        if self.head is None:
            raise ValueError("lista jest pusta")
        node1 = after.next
        node2 = node1.next
        after.next = node2

    def __len__(self):
        node = self.head
        if self.head is not None:
            x = 1
            while node.next:
                node = node.next
                x += 1
            return x
        return 0

    def __str__(self):
        node = self.head
        string = ""
        while node is not None:
            string += str(node.value)
            if node.next is not None:
                string += " -> "
            node = node.next
        return string


list_ = LinkedList()
assert list_.head is None
list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'
print("Funkcja print:")
print(list_)
list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element

assert str(list_) == '1 -> 5 -> 9'
second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'
print("Funkcja len:")
print(len(list_))
print("\n")


class Stack:
    _storage: LinkedList()

    def __init__(self):
        self.head = None

    def push(self, element: Any) -> None:
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> Any:
        if self.head is not None:
            current = self.head
            self.head = current.next
            return current.value
        else:
            raise ValueError("Stos jest pusty")

    def __str__(self):
        node = self.head
        string = ""
        while node is not None:
            string += str(node.value)
            if node.next is not None:
                string += "\n"
            node = node.next
        return string

    def __len__(self):
        node = self.head
        if self.head is not None:
            x = 1
            while node.next is not None:
                node = node.next
                x += 1
            return x
        return 0


stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2
print("Funkcja print: ")
print(stack)
print("Funkcja len: ")
print(len(stack))
print("\n")


class Queue:
    _storage: LinkedList

    def __init__(self):
        self.head = None

    def peek(self) -> Any:
        node = self.head
        if node is None:
            print("empty")
        return node.value

    def enqueue(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is not None:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            return
        self.head = new_node

    def dequeue(self) -> Any:
        if self.head is not None:
            current = self.head
            self.head = current.next
            return current.value
        raise ValueError("Kolejka jest pusta")

    def __len__(self):
        node = self.head
        if self.head is not None:
            x = 1
            while node.next is not None:
                node = node.next
                x += 1
            return x
        return 0

    def __str__(self):
        node = self.head
        string = ""
        while node is not None:
            string += str(node.value)
            if node.next is not None:
                string += ", "
            node = node.next
        return string


queue = Queue()

assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
print("Funkcja print: ")
print(queue)
print("Funkcja len: ")
print(len(queue))
