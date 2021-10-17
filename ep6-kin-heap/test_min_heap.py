from min_heap import MinHeap

h = MinHeap()
h.print()
print("min: ", h.min())

h.insert(3)
h.print()
print("min: ", h.min())

h.insert(4)
h.print()
print("min: ", h.min())

h.insert(6)
h.print()
print("min: ", h.min())

h.insert(1)
h.print()
print("min: ", h.min())

h.insert(0)
h.print()
print("min: ", h.min())

h.insert(5)
h.print()
print("min: ", h.min())

print("\n----------((***))----------\n")

h.del_min()
h.print()
print("min: ", h.min())

h.del_min()
h.print()
print("min: ", h.min())

h.del_min()
h.print()
print("min: ", h.min())

comp = lambda x, y: x[1] - y[1]
h = MinHeap(comparator=comp)
h.print()
print("min: ", h.min())

h.insert(('b', 5))
h.print()
print("min: ", h.min())

h.insert(('x', 3))
h.print()
print("min: ", h.min())

h.insert(('m', 6))
h.print()
print("min: ", h.min())

h.insert(('z', 1))
h.print()
print("min: ", h.min())

h.insert(('r', 4))
h.print()
print("min: ", h.min())

h.insert(('s', 0))
h.print()
print("min: ", h.min())

print("\n----------((***))----------\n")

h.del_min()
h.print()
print("min: ", h.min())

h.del_min()
h.print()
print("min: ", h.min())

h.del_min()
h.print()
print("min: ", h.min())
