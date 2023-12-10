input = """Time:        46     68     98     66
Distance:   358   1054   1807   1080"""

data = [n for line in input.split('\n') for n in line.split(' ') if n.isdigit()]
print(data)

up = ''
bot = ''
for i in range(0, int(len(data)/2)):
  up += data[i]
  bot += data[i+4]


print(up, bot)

def findWays(time, distance):
  result, c = [], 0

  while c < time:
    hold = time - c
    rtime = time - hold
    if hold * rtime > distance:
      result.append(rtime)
    c += 1

  return len(result)

print(findWays(int(up), int(bot)))
  