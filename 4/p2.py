input = """"""

input = (input.replace('\nCard', '')).split(' ')

new = []
for i in input:
  try:
    int(i)
    new.append(int(i))
  except:
    continue

final_sum, lines, i = 0, 0, 0

test = []
while lines < (len(new) / 35):

  matching = 0
  
  winning = new[i:i+10]
  nums = new[i+10:i+35]
  
  for num in nums:
    if num in winning:
      matching += 1

  i += 35
  lines += 1

  test.append([1, matching])

start = 1
for card in test:
  actual = start

  num_of_cards = card[0]
  matchings = card[1]

  while actual < matchings + start:
    test[actual][0] += 1 * num_of_cards
    actual+= 1

  start +=1

sum_num_of_cards = 0
for card in test: sum_num_of_cards += card[0]

print(sum_num_of_cards)
