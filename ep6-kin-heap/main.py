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


def move_to(h, t):
  h.advance(t)
  h.print()
  print(f"★★★ max at {t}: {h.max().id}")

h = KinHeap(
  extract('id', lines),
  extract('x0', lines),
  extract('v', lines),
  len(lines)
)
h.print()

move_to(h, 2)
move_to(h, 6)
move_to(h, 12)
move_to(h, 17)

# p4 takes the lead at  30
h.change(3, 1)
h.print()

move_to(h, 30)  # p2 leads still
move_to(h, 31)  # p4 takes the lead

# p1 takes the lead at ~45
h.change(2, 1.5)

move_to(h, 40)  # p4 is still the leader
move_to(h, 45)  # p1 takes the lead

h.insert('p5', 35, 3) # p5 takes the lead at ~65
h.print()

move_to(h, 66) # p5 is the lead

# h.del_max() # p4 is removed then p1 becomes leader again
# print(f"★★★ new max is {h.max()}")
