from vs import VS
from pprint import pprint
from termcolor import colored


def check(s, f, e):
  print()
  if e == f:
    print(colored(f"✅  [P={s}]  expected: {e} | found: {f}", 'green'))
  else:
    print(colored(f"🚩  [P={s}]  expected: {e} | found: {f}", 'red'))
  print("--------------------------------------")


def test_0():
  T = "abracadabra"

  print(f"TEST 0: {T}")

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

  check("LCP",  s.lcp,        [0, 0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2])
  check("Suff", s.suffixes,   [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2])
  print()


def test_1():
  print("\n\n\n##############################################")

  T = "AAACCTTTGCGACC"

  print(f"TEST 1: {T}")

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

  check("LCP",  s.lcp,        [0, 0, 2, 1, 3, 0, 1, 2, 1, 1, 0, 1, 0, 1, 2])
  check("Suff", s.suffixes,   [14, 0, 1, 11, 2, 13, 12, 3, 9, 4, 10, 8, 7, 6, 5])


def test_2():
  print("\n\n\n##############################################")

  T = "AAACCATTGCGACC"

  print(f"TEST 2: {T}")

  s = VS(T)
  s.print()

  #  14 – '$'
  #  0  – 'AAACCATTGCGACC$'
  #  1  – 'AACCATTGCGACC$'
  #  11 – 'ACC$'
  #  2  – 'ACCATTGCGACC$'
  #  5  – 'ATTGCGACC$'
  #  13 – 'C$'
  #  4  – 'CATTGCGACC$'
  #  12 – 'CC$'
  #  3  – 'CCATTGCGACC$'
  #  9  – 'CGACC$'
  #  10 – 'GACC$'
  #  8  – 'GCGACC$'
  #  7  – 'TGCGACC$'
  #  6  – 'TTGCGACC$'

  check("LCP",  s.lcp,        [0, 0, 2, 1, 3, 1, 0, 1, 1, 2, 1, 0, 1, 0, 1])
  check("Suff", s.suffixes,   [14, 0, 1, 11, 2, 5, 13, 4, 12, 3, 9, 10, 8, 7, 6])


def test_3():
  print("\n\n\n##############################################")

  T = "AAT"

  print(f"TEST 3: {T}")

  s = VS(T)
  s.print()

  check("LCP",  s.lcp,      [0, 0, 1, 0])
  check("Suff", s.suffixes, [3, 0, 1, 2])


test_0()
test_1()
test_2()
test_3()