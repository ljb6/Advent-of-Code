input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

data = input.split('\n')

final_sum = 0
for line in data:

  tree = [line.split(' ')]

  c = 0
  while all(i == 0 for i in tree[len(tree) - 1]) != True:
    lc = 0
    add = []

    while lc < (len(tree[c]) - 1):
      add.append(int(tree[c][lc + 1]) - int(tree[c][lc]))
      lc += 1
    
    tree.append(add)
    c += 1

  tree = tree[::-1]
  
  sum = []
  for i in tree: sum.append(int(i[len(i) - 1]))
  
  print(sum)
  
  for i in sum:
    final_sum += i
  
print(final_sum)




