from heap import Heap

comp = lambda x, y: x[1] - y[1]

h = Heap(nature="min", comparator=comp)
h.print()
print("min: ", h.min())

# INFO: throws errors!
# print("max: ", h.max())
# print("del_max: ", h.del_max())

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

h.del_min()
h.print()
print("min: ", h.min())

h.del_min()
h.print()
print("min: ", h.min())

h.del_min()
h.print()
print("min: ", h.min())

print("\n\n\n")

h = Heap(nature="max", comparator=comp)
h.print()
print("max: ", h.max())

# INFO: throws errors!
# print("min: ", h.min())
# print("del_min: ", h.del_min())

h.insert(('b', 5))
h.print()
print("max: ", h.max())

h.insert(('x', 3))
h.print()
print("max: ", h.max())

h.insert(('m', 6))
h.print()
print("max: ", h.max())

h.insert(('z', 1))
h.print()
print("max: ", h.max())

h.insert(('r', 4))
h.print()
print("max: ", h.max())

h.insert(('s', 7))
h.print()
print("max: ", h.max())

h.del_max()
h.print()
print("max: ", h.max())

h.del_max()
h.print()
print("max: ", h.max())

h.del_max()
h.print()
print("max: ", h.max())
