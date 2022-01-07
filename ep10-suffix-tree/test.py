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

  s = AS(T, "abcdr")

  print()
  print(s.search("a"))            # True
  print(s.search("cada"))         # True
  print(s.search("abracadabra"))  # True
  print(s.search("abro"))         # False
  print(s.search("cadabro"))      # False
  print(s.search("roca"))         # False
  print(s.search("xoca"))         # False

  print()
  print(s.num_occurrences("a"))            # 5
  print(s.num_occurrences("bra"))          # 2
  print(s.num_occurrences("cada"))         # 1
  print(s.num_occurrences("abracadabra"))  # 1
  print(s.num_occurrences("abro"))         # 0
  print(s.num_occurrences("xoca"))         # 0

  print()
  print(s.occurrences("a"))            # [10, 7, 0, 3, 5]
  print(s.occurrences("bra"))          # [8, 1]
  print(s.occurrences("cada"))         # [4]
  print(s.occurrences("abracadabra"))  # [0]
  print(s.occurrences("abro"))         # []
  print(s.occurrences("xoca"))         # []

  s.print(include_extra=True)

  print("\n\n")


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

  s = AS(T, "ACGT")

  print()
  print(s.search("CC"))           # True
  print(s.search("CCTTTGC"))      # True
  print(s.search("TTTGCGACC"))    # True
  print(s.search("AGACT"))        # False
  print(s.search("TTGCGACA"))     # False

  print()
  print(s.num_occurrences("A"))           # 4
  print(s.num_occurrences("CC"))          # 2
  print(s.num_occurrences("TTTGCGACC"))   # 1
  print(s.num_occurrences("AGACT"))       # 0
  print(s.num_occurrences("TTGCGACA"))    # 0

  print()
  print(s.occurrences("A"))             # [0, 1, 11, 2]
  print(s.occurrences("CC"))            # [12, 3]
  print(s.occurrences("TTTGCGACC"))     # [5]
  print(s.occurrences("AGACT"))         # []
  print(s.occurrences("TTGCGACA"))      # []

  s.print()


test_0()
test_1()
