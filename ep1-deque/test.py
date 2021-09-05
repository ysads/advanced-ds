import unittest
from deque import deque, print_deque, push_front, push_back, pop_front, pop_back, kth, back, front, lowest_common_ancestor

class TestDeque(unittest.TestCase):
  def assert_equal(self, *args):
    return self.assertEqual(*args)


  def assert_topology(self, d, topo):
      if (d.size == 1):
        return self.assert_equal(topo, 'node')

      lca = lowest_common_ancestor(d.front, d.back)
  
      if lca == d.front:
        self.assert_equal(topo, 'lean-right')
      elif lca == d.back:
        self.assert_equal(topo, 'lean-left')
      else:
        self.assert_equal(topo, 'v-shape')


  def test_t1(self):
    """
    Test operations on empty and nearly-empty deques.
    """
    d0 = deque()
    d1 = push_back(d0, 3)
    d2 = pop_front(d1)

    self.assert_equal(print_deque(d0), [])
    self.assert_equal(front(d0), None)
    self.assert_equal(back(d0), None)

    self.assert_equal(print_deque(d1), [3])
    self.assert_equal(front(d1), 3)
    self.assert_equal(back(d1), 3)

    self.assert_equal(print_deque(d2), [])
    self.assert_equal(front(d2), None)
    self.assert_equal(back(d2), None)


  def test_t2(self):
    """
    V-shaped deque with a single element on left branch. Tests if pop_front
    moves front pointer to right branch, as well as pop_back and pop_front
    on linear right-leaning deques.
    """
    d0 = deque()            # []
    d1 = push_front(d0, 3)  # [3]
    d2 = push_front(d1, 9)  # [9, 3]
    d3 = push_back(d2, 10)  # [9, 3, 10]
    d4 = push_back(d3, 11)  # [9, 3, 10, 11]
    d5 = push_back(d4, 12)  # [9, 3, 10, 11, 12]
    d6 = push_back(d5, 13)  # [9, 3, 10, 11, 12, 13]

    self.assert_equal(print_deque(d6), [9, 3, 10, 11, 12, 13])
    self.assert_equal(front(d6), 9)
    self.assert_equal(back(d6), 13)
    self.assert_topology(d6, 'v-shape')

    self.assert_equal(kth(d6, 1), 9)
    self.assert_equal(kth(d6, 3), 10)

    d7 = pop_front(d6)      # [3, 10, 11, 12, 13]

    self.assert_equal(print_deque(d7), [3, 10, 11, 12, 13])
    self.assert_equal(front(d7), 3)
    self.assert_equal(back(d7), 13)
    self.assert_topology(d7, 'lean-right')

    self.assert_equal(kth(d7, 1), 3)
    self.assert_equal(kth(d7, 4), 12)

    d8 = pop_front(d7)      # [10, 11, 12, 13]

    self.assert_equal(print_deque(d8), [10, 11, 12, 13])
    self.assert_equal(front(d8), 10)
    self.assert_equal(back(d8), 13)
    self.assert_topology(d7, 'lean-right')

    d9 = pop_back(d8)      # [10, 11, 12]

    self.assert_equal(print_deque(d9), [10, 11, 12])
    self.assert_equal(front(d9), 10)
    self.assert_equal(back(d9), 12)
    self.assert_topology(d7, 'lean-right')

  def test_t3(self):
    """
    V-shaped deque with a single element on the *right* branch. It's the
    symmetric equivalent of t3. Test if pop_back also moves the back pointer
    to the left branch.
    """
    d0 = deque()            # []
    d1 = push_back(d0, 4)   # [4]
    d2 = push_back(d1, 5)   # [4, 5]
    d3 = push_front(d2, 3)  # [3, 4, 5]
    d4 = push_front(d3, 2)  # [2, 3, 4, 5]

    self.assert_equal(print_deque(d4), [2, 3, 4, 5])
    self.assert_equal(front(d4), 2)
    self.assert_equal(back(d4), 5)
    self.assert_topology(d4, 'v-shape')

    d5 = pop_back(d4)       # [2, 3, 4]

    self.assert_equal(print_deque(d5), [2, 3, 4])
    self.assert_equal(front(d5), 2)
    self.assert_equal(back(d5), 4)
    self.assert_topology(d5, 'lean-left')

    d6 = push_back(d5, 6)   # [2, 3, 4]

    self.assert_equal(print_deque(d6), [2, 3, 4, 6])
    self.assert_equal(front(d6), 2)
    self.assert_equal(back(d6), 6)
    self.assert_topology(d6, 'v-shape')


  def test_t4(self):
    """
    Complex deque with several arborescences. Test if access to previous
    states of the deque remain as expected as well as if kth traverses
    the correct trees.
    """
    d0 = deque()            # []
    d1 = push_back(d0, 3)   # [3]
    d2 = push_back(d1, 4)   # [3, 4]
    d3 = push_front(d2, 2)  # [2, 3, 4]
    d4 = push_front(d3, 1)  # [1, 2, 3, 4]
    d5 = pop_back(d3)       # [2, 3]
    d6 = pop_back(d5)       # [2]
    d7 = push_front(d6, 9)  # [9, 2]
    d8 = pop_front(d6)      # []
    d9 = push_front(d8, 6)  # [6]

    self.assert_equal(print_deque(d4), [1, 2, 3, 4])
    self.assert_equal(print_deque(d5), [2, 3])
    self.assert_equal(print_deque(d7), [9, 2])
    self.assert_equal(print_deque(d8), [])
    self.assert_equal(print_deque(d9), [6])

    self.assert_equal(kth(d2, 2), 4)
    self.assert_equal(kth(d3, 1), 2)
    self.assert_equal(kth(d4, 3), 3)
    self.assert_equal(kth(d4, 4), 4)
    self.assert_equal(kth(d7, 1), 9)
    self.assert_equal(kth(d9, 1), 6)


unittest.main()