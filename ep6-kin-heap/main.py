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
move_to(h, 35)
