# Linked List

A simple Python implementation of a **singly linked list** data structure.

## Features

- Add elements to the end or beginning of the list
- Insert or remove elements at any position
- Access elements by index
- Get the current list size
- Educational, beginner-friendly code

## Usage

1. Download or clone this repository.
2. Use the `LinkedList` class in your project, for example:

   ```python
   from LinkedList import LinkedList

   ll = LinkedList()
   ll.append(10)
   ll.insert_begin(5)
   ll.insert_position(15, 1)
   print(ll.get_size())
   print(ll[1].value)  # Get value of the second node
