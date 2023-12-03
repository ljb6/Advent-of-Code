input = """"""

syms = ['@', '#', '$', '%', '&', '*', '-', '/', '=', '+']

engine = input.split('\n')
engine.insert(0, '.' * 140)
engine.insert(141, '.' * 140)

print(engine)
final_sum = 0
for line in range(1, 140):
    
    index = 0
    while index < 139:
        
        first_pos = index

        try:
            int(engine[line][index])
            try:
                int(engine[line][index + 1])
                try: #3c
                    int(engine[line][index + 2])
                    num = engine[line][index] + engine[line][index + 1] + engine[line][index + 2]
                    index += 2
                except: #2c
                    num = engine[line][index] + engine[line][index + 1]
                    index += 1
            except: # 1c
                num = engine[line][index]
        except:
            num = 0

        last_pos = first_pos + len(str(num)) - 1
        first_pos = last_pos - len(str(num))

        if num != 0:
          if first_pos == -1:
            test = str(engine[line - 1][first_pos + 1:last_pos + 2] + engine[line][first_pos + 1:last_pos + 2] + engine[line + 1][first_pos + 1:last_pos + 2])
          elif last_pos == 139:
            test = str(engine[line - 1][first_pos:last_pos + 1] + engine[line][first_pos:last_pos + 1] + engine[line + 1][first_pos:last_pos + 1])
          else:
            test = str(engine[line - 1][first_pos:last_pos + 2] + engine[line][first_pos:last_pos + 2] + engine[line + 1][first_pos:last_pos + 2])

          for i in test:
            if i in syms:
               final_sum += int(num)
               break

        index += 1

print(final_sum)