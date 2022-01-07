from suffix_tree import AS
from pprint import pprint
from termcolor import colored


def check(s, f, e):
  print()
  if e == f:
    print(colored(f"✅  [P={s}]  expected: {e} | found: {f}", 'green'))
  else:
    print(colored(f"🚩  [P={s}]  expected: {e} | found: {f}", 'red'))
  print("\n--------------------------------------\n")


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
  # s.print()

  print()
  check("a",            s.search("a"),            True)
  check("bra",          s.search("bra"),          True)
  check("bracadabra",   s.search("bracadabra"),   True)
  check("abracadabra",  s.search("abracadabra"),  True)
  check("adabra",       s.search("adabra"),       True)
  check("cada",         s.search("cada"),         True)
  check("abro",         s.search("abro"),         False)
  check("cadabro",      s.search("cadabro"),      False)
  check("rocadabra",    s.search("rocadabra"),    False)
  check("xocadabra",    s.search("xocadabra"),    False)

  check("a",            s.num_occurrences("a"),             5)
  check("bra",          s.num_occurrences("bra"),           2)
  check("bracadabra",   s.num_occurrences("bracadabra"),    1)
  check("abracadabra",  s.num_occurrences("abracadabra"),   1)
  check("adabra",       s.num_occurrences("adabra"),        1)
  check("cada",         s.num_occurrences("cada"),          1)
  check("abro",         s.num_occurrences("abro"),          0)
  check("cadabro",      s.num_occurrences("cadabro"),       0)
  check("rocadabra",    s.num_occurrences("rocadabra"),     0)
  check("xocadabra",    s.num_occurrences("xocadabra"),     0)

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
  s.print()

  print()


test_0()
# test_1()
