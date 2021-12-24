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
  s.print(include_lrlcp=True)

  print()
  print(s.search("racadabra"))
  print(s.search("racadabre"))
  print(s.search("zabra"))
  print(s.search("abracadabro"))
  print(s.search("cenabra"))
  print(s.search("cadabra"))
  print(s.search("adobra"))
  print(s.search("adabra"))
  print(s.search("abra"))


def test_1():
  print("\n\n\n##############################################")

  T = open("test_1.txt", "r").read()

  print(f"TEST 1: {T}")
  print("\n-------------------------------------- ")

  s = VS(T)
  s.print(include_lrlcp=True)

  print()
  s.search("ACCTG")
  s.search("GCCTG")
  s.search("CCTTTGCGAC")


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

  s = VS(T)
  s.print()

  print()
  print(s.search("zad"))
  print(s.search("abr"))
  print(s.search("bra"))
  print(s.search("bro"))
  print(s.search("cabra"))



test_0()
test_1()
test_2()
