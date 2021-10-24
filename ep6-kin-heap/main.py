"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!

This examples showcases the usage of a kinectic heap. Commenting all lines
and running them incrementally helps visualizing what's happening. Note that
`change` operation relies on the moment it runs to add the new point, thus
calling it in other places alters completely the state of the heap.
"""
from kin_heap import KinHeap

lines = [
  {
    'id': 'p3',
    'x0': 17,
    'v':  -0.5
  },
  {
    'id': 'p1',
    'x0': 16,
    'v':  0
  },
  {
    'id': 'p4',
    'x0': 3,
    'v':  0.4
  },
  {
    'id': 'p2',
    'x0': 8,
    'v':  0.5
  },
]

def extract(feat, coll):
  return list(map(lambda x: x[feat], coll))

h = KinHeap(
  extract('id', lines),
  extract('x0', lines),
  extract('v', lines),
  len(lines)
)
h.print()

# We run this, nothing changes at t=2 and p2 takes the lead at t=9
# h.delete('p1')
# h.print()

h.advance(1)
h.advance(2)
h.print()

h.advance(17)
h.print()

# p4 takes the lead a little after 30
h.change(3, 1)
h.print()

h.advance(30)  # p2 leads still
h.print()

h.advance(31)  # p4 takes the lead
h.print()

# p1 takes the lead a little before 47
h.change(2, 1.5)

h.advance(40)  # p4 is still the leader
h.print()

h.advance(47)  # p1 takes the lead
h.print()

# p5 takes the lead at ~55
h.insert('p5', 32, 2.5)
h.print()

h.advance(54) # p1 still leads
h.print()

h.advance(56) # p5 is the lead
h.print()

# p3 takes the lead:
# - at ~82,   if we remove p5
# - at ~100,  if we mantain p5
h.change(4, 4)
h.print()

h.del_max() # p5 removed, p1 becomes leader again
h.print()

h.advance(81)  # p1 leads
h.print()

h.advance(82)  # p3 now leads
h.print()

h.delete('p1')
h.print()
