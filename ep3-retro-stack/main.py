"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from retro_stack import *
from re import sub

def sanitize(x):
  return x if x == '' else int(x.strip())


def parse(line):
  cmd, rest = line.split('(')
  args = list(map(sanitize, sub(r'\).*', '', rest).split(',')))

  return cmd, args


def execute(cmd, args, stack_root):
  if cmd == "Stack":
    stack_root = stack()
  elif cmd == "Push":
    stack_root = push(stack_root, args[0], args[1])
  elif cmd == "Pop":
    stack_root = pop(stack_root, args[0])
  elif cmd == "Delete":
    stack_root = delete(stack_root, args[0])
  elif cmd == "Size":
    print(size(stack_root, args[0]))
  elif cmd == "Top":
    print(top(stack_root, args[0]))
  elif cmd == "Kth":
    print(kth(stack_root, args[0]))
  elif cmd == "Print":
    print_stack(stack_root)
  
  return stack_root


stack_root = None
print("Type `quit` to exit the runner.")
while True:
  try:
    line = input()

    if line == 'quit':
      break
    if line == '':
      continue
    
    cmd, args = parse(line)
    stack_root = execute(cmd, args, stack_root)

  except EOFError:
    break
