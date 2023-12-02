input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

input = input.replace(':', ';')
input = input.replace(',', '')
input = input.replace('   ', ' ')
games = input.split('\n')

sum_ids = 0
for game in games:
    
    check = []
    game = game.split(';')
    
    for i in game:
        check.append(i.split(' '))
    
    external = len(check) - 1
    
    test = 0
    while external > 0:
        internal = len(game[external].split(' ')) - 1
        points = {'blue': 0, 'red': 0, 'green': 0}

        while internal > 0:
            points[check[external][internal]] += int(check[external][internal - 1])
            internal -= 2

        external -= 1

        if points['red'] <= 12 and points['green'] <= 13 and points['blue'] <= 14:
            test += 1
    
    if (len(check) - 1) == test:
        sum_ids += int(check[0][1])

print('Sum:', sum_ids)
