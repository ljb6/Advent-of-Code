input = """Game 1: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red
Game 2: 6 red, 6 blue, 2 green; 1 blue, 1 red; 6 green, 1 red, 10 blue
Game 3: 1 green, 2 blue; 7 blue, 4 green; 2 green, 1 blue; 10 blue, 4 green; 4 blue; 1 green, 7 blue, 1 red
Game 4: 16 red, 12 blue, 10 green; 15 red, 5 green, 6 blue; 10 green, 15 red, 12 blue
Game 5: 2 green, 2 red, 9 blue; 1 red, 5 green; 4 green, 12 blue, 1 red; 5 blue, 8 green
"""

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
    
    points = {'blue': 0, 'red': 0, 'green': 0}
    while external > 0:
        internal = len(game[external].split(' ')) - 1

        while internal > 0:
            if points[check[external][internal]] < int(check[external][internal - 1]):
                points[check[external][internal]] = int(check[external][internal - 1])
            internal -= 2

        external -= 1
    
    sum_ids += points['blue'] * points['red'] * points['green']

print('Sum:', sum_ids)
