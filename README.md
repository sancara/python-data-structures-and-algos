# Python Data Structures & Algorithms

# Data Structures

## Nodes

- have data and link to next node
- if the link is None, we are at the end of the node path we were following
- img

## Linked List

- uni or bidirectional
- comprised of nodes
- head and tail nodes
- data and link to next node

## Double Linked List

- comprised of nodes
- two pointers:
  - one for next node
  - one for previous node
- head previous node is set to null
- tail next node is set to null

## Queues

- comprised of nodes
- three main operations:
  - enqueue: add data to the back
  - dequeue: remove and provide data from the front
  - peek: shows data from the front
- implemented as an array | linked list
- bounded queue has a limited size
- enqueue on a full queue causes overflow
- dequeue on an empty queue causes underflow
- queue process data -> first in, first out FIFO
  ## Stack
- contains ordered set of data
- can have a limited size
- perform better on linked lists than arrays
- methods:
  - Push: adds data to the top of the stack
  - Pop: returns and removes data from the top of the stack
  - Peek: returns data from the top of the stack
- last in, first out -> (LIFO)
