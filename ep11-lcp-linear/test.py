"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from vs import VS

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

  s = VS(T)
  s.print()

  # LCP       => [0, 0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2]
  # Suffixes  => [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]

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

  s = VS(T)
  s.print()

  # LCP       => [0, 0, 2, 1, 3, 0, 1, 2, 1, 1, 0, 1, 0, 1, 2]
  # Suffixes  => [14, 0, 1, 11, 2, 13, 12, 3, 9, 4, 10, 8, 7, 6, 5]


test_0()
test_1()
