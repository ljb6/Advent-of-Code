input = """"""

symbols = ['@', '#', '$', '%', '&', '*', '-', '/', '=', '+']
total_sum = 0
engine = input.splitlines()
engine.insert(0, '.' * 140)
engine.insert(141, '.' * 140)

new_engine = []
for line in engine:
  new_engine.append('.' + line + '.')

def find_symbols(line):
  cords = []

  j = 0
  for i in line:
    if i in symbols:
      cords.append(j)
    j += 1
  
  return cords

def find_nums(line):
  nums_and_cords = {}
  num = ''

  i = 0
  while i < len(line) - 1:
    
    if line[i].isdigit():
      num += line[i]
      start, end = i, i
      if line[i + 1].isdigit():
        num += line[i + 1]
        i += 1
        end = i
        if line[i + 1].isdigit():
          num += line[i + 1]
          i += 1
          end = i
    
    if num:
      start -= 1
      end += 1

      res = []
      while start < (end + 1):
        res.append(start)
        start += 1
      nums_and_cords[num] = res


    num = ''
    i += 1

  return nums_and_cords
  
print('')

j = 0
for line in range(0, (len(new_engine))):

  for key, value in find_nums(new_engine[line]).items():

    check = find_symbols(new_engine[line - 1]) + find_symbols(new_engine[line]) + find_symbols(new_engine[line + 1]) 

    for c in check:
      if c in value:
        total_sum += int(key)
        break

    j += 1

print(total_sum)
