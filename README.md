# Linked List Implementations in Python

This project contains simple implementations of **singly** and **doubly** linked lists in Python. It includes `LinkedList` and `DoublyLinkedList` classes with common operations such as `append`, `pop`, `insert`, `remove`, and `reverse`.

---

## 📦 Structure

- `linked_list.py` – Singly linked list
- `doubly_linked_list.py` – Doubly linked list
- `node.py` – Contains `SinglyNode` and `DoublyNode` classes

---

## 🔧 LinkedList Class Overview (Singly Linked List)

### Initialization

```python
ll = LinkedList(10)
```

Creates a new singly linked list with an initial node of value `10`.

### Methods

- 🔁 `print_list()` – Prints all node values
- ➕ `append(value)` – Adds to the end
- ➖ `pop()` – Removes from the end
- 🔼 `prepend(value)` – Adds to the beginning
- 🔽 `pop_first()` – Removes from the beginning
- 🔍 `get(index)` – Gets node at index
- ✏️ `set_value(index, value)` – Sets value at index
- ➕ `insert(index, value)` – Inserts at index
- ❌ `remove(index)` – Removes node at index
- 🔁 `reverse()` – Reverses the list

---

## 🔧 DoublyLinkedList Class Overview

### Initialization

```python
dll = DoublyLinkedList(10)
```

Creates a new doubly linked list with an initial node of value `10`.

### Methods

- 🔁 `print_list()` – Prints all node values
- ➕ `append(value)` – Adds to the end
- ➖ `pop()` – Removes from the end
- 🔼 `prepend(value)` – Adds to the beginning
- 🔽 `pop_first()` – Removes from the beginning
- 🔍 `get(index)` – Gets node at index
- ✏️ `set_value(index, value)` – Sets value at index
- ➕ `insert(index, value)` – Inserts at index
- ❌ `remove(index)` – Removes node at index
- 🔁 `reverse()` – Reverses the list

---

## ✅ Example Usage

### Singly Linked List

```python
from linked_list import LinkedList

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 2 3

ll.pop()
ll.print_list()  # Output: 1 2

ll.prepend(0)
ll.print_list()  # Output: 0 1 2

ll.reverse()
ll.print_list()  # Output: 2 1 0
```

### Doubly Linked List

```python
from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList(5)
dll.append(6)
dll.prepend(4)
dll.print_list()  # Output: 4 5 6

dll.pop()
dll.print_list()  # Output: 4 5

dll.insert(1, 10)
dll.print_list()  # Output: 4 10 5
```

---

## 📜 License

This code is free to use for personal or educational projects. Attribution is appreciated.
