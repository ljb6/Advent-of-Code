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
  
  sum = []
  for i in tree: sum.append(int(i[0]))
  sum.reverse()

  sumup = 0
  new_col = [0 for i in sum]

  for i in range(0, (len(sum))):
    try:
      new_col[i + 1] = sum[i + 1] - new_col[i]
    except:
      final_sum += new_col[len(new_col) - 1]

print(final_sum)




