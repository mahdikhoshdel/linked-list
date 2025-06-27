---

# Linked List Implementation in Python

This project contains a simple implementation of a **singly linked list** in Python. It defines a `LinkedList` class with common operations such as append, pop, insert, remove, and reverse.

---

## 🔧 LinkedList Class Overview

### Initialization

```python
ll = LinkedList(10)
```

Creates a new linked list with an initial node of value `10`.

---

### Methods

#### 🔁 `print_list()`

Prints all node values in the list.

#### ➕ `append(value)`

Adds a node with the given value at the end of the list.

#### ➖ `pop()`

Removes the last node and returns it.

#### 🔼 `prepend(value)`

Adds a node with the given value at the beginning.

#### 🔽 `pop_first()`

Removes the first node and returns it.

#### 🔍 `get(index)`

Returns the node at the specified index, or `None` if out of bounds.

#### ✏️ `set_value(index, value)`

Updates the value of the node at the given index.

#### ➕ `insert(index, value)`

Inserts a node at the given index. Returns `True` on success, `None` if the index is invalid.

#### ❌ `remove(index)`

Removes the node at the specified index and returns it.

#### 🔁 `reverse()`

Reverses the order of the linked list in-place.

---

## ✅ Example Usage

```python
from linked_list import LinkedList

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.print_list()   # Output: 1 2 3

ll.pop()
ll.print_list()   # Output: 1 2

ll.prepend(0)
ll.print_list()   # Output: 0 1 2

ll.reverse()
ll.print_list()   # Output: 2 1 0
```

## 📜 License

This code is open for personal or educational use. Attribution is appreciated.

---
