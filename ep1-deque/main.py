from deque import *

d0 = deque()
d1 = push_back(d0, 3)
d2 = push_back(d1, 4)
d3 = push_front(d2, 2)
d4 = push_front(d3, 1)
d5 = pop_back(d3) 
d6 = pop_back(d5)
d7 = push_front(d6, 9)
d8 = pop_front(d6)
d9 = push_front(d8, 6)

print_deque(d3)   # [2, 3, 4]
print(front(d3))  # 2
print(back(d3))   # 4
print(kth(d3, 2)) # 3

print_deque(d7)   # [9, 2]
print(front(d7))  # 9
print(back(d7))   # 2
print(kth(d7, 1)) # 9

print_deque(d4)   # [1, 2, 3, 4]
print(front(d4))  # 1
print(back(d4))   # 4
print(kth(d4, 3)) # 3
print(kth(d4, 2)) # 2

print_deque(d8)   # []
print(front(d8))  # None
print(back(d8))   # None

print_deque(d9)   # [6]
print(front(d9))  # 6
print(back(d9))   # 6