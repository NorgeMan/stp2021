# v1
from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:', stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack elements are popped:', stack)

# v2
from queue import LifoQueue

stack = LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')

print('Full:', stack.full())
print('Size:', stack.qsize())
print('\nStack elements are popped:')
print(stack.get())
print(stack.get())
print(stack.get())

print('\nEmpty:', stack.empty())