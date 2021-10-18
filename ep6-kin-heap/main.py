from kin_heap import KinHeap

id    = [1,  2,   3,    4]
x0    = [16, 8,   17,   3]
speed = [0,  0.5, -0.5, 0.25]

h = KinHeap(id, x0, speed, len(id))
h.print()

print(h.max())
h.advance(1)
h.advance(2)
h.advance(6)
h.advance(10)
h.advance(12)
