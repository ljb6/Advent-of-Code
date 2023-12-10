input = """0 3 6 9 12 15"""

data = input.split('\n')
#print(data)

for line in data:

  tree = [line.split(' ')]

  c = 0
  while c < len(tree[0]):
    
