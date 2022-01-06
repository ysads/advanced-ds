"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from suffix_tree import AS

def test_0():
  T = open("test_0.txt", "r").read()

  print(f"TEST 0: {T}")
  print("\n-------------------------------------- ")

  # ['0 – $',
  # '1 – a$',
  # '2 – abra$',
  # '3 – abracadabra$',
  # '4 – acadabra$',
  # '5 – adabra$',
  # '6 – bra$',
  # '7 – bracadabra$',
  # '8 – cadabra$',
  # '9 – dabra$',
  # '10 – ra$',
  # '11 – racadabra$']

  s = AS(T)
  s.print()

  print("\n\n")
  s.suffix_tree_root.walk_inorder()

  print()


def test_1():
  print("\n\n\n##############################################")

  T = open("test_1.txt", "r").read()

  print(f"TEST 1: {T}")
  print("\n-------------------------------------- ")

  # ['0 – $',
  # '1 – AAACCTTTGCGACC$',
  # '2 – AACCTTTGCGACC$',
  # '3 – ACC$',
  # '4 – ACCTTTGCGACC$',
  # '5 – C$',
  # '6 – CC$',
  # '7 – CCTTTGCGACC$',
  # '8 – CGACC$',
  # '9 – CTTTGCGACC$',
  # '10 – GACC$',
  # '11 – GCGACC$',
  # '12 - TGCGACC',
  # '13 - TTGCGACC',
  # '14 - TTTGCGACC']

  s = AS(T)

  print("\n\n")
  s.suffix_tree_root.walk_inorder()
  s.print()

  print()


def test_2():
  print("\n\n\n##############################################")

  T = open("test_2.txt", "r").read()

  print(f"TEST 2: {T}")
  print("\n-------------------------------------- ")

  # ['0 – $',
  #  '1 – a$',
  #  '2 – abra$',
  #  '3 – bra$',
  #  '4 – cabra$',
  #  '5 – ra$']

  s = AS(T)
  s.print()

  print()



test_0()
test_1()
# test_2()
