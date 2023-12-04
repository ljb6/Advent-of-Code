input = """Card   1: 13  4 61 82 80 41 31 53 50  2 | 38 89 26 79 94 50  2 74 31 92 80 41 13 97 61 82 68 45 64 39  4 53 90 84 54
"""

input = (input.replace('\nCard', '')).split(' ')

new = []
for i in input:
  try:
    int(i)
    new.append(int(i))
  except:
    continue

final_sum, lines, i = 0, 0, 0
while lines < (len(new) / 35):

  sumup = 0
  winning = new[i:i+10]
  nums = new[i+10:i+35]
  

  for num in nums:
    if num in winning:
      if sumup == 0:
        sumup = 1
      else:
        sumup *= 2

  final_sum += sumup
  i += 35
  lines += 1

print(final_sum)