input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

lista = input.split('\n')

writed = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


sum = 0
for line in lista:
    
    nums = []
    
    pos = 0
    for i in line:
  
        try:
            test = int(i)
            nums.append(i)
        except:
            c = 0
            while c < 6:
                #print(line[pos:pos + c])
                if line[pos:pos + c] in writed.keys():
                    #print('True, pos:', pos, line[pos:pos + c])
                    nums.append(writed[line[pos:pos + c]])
                c += 1
            pass
        pos += 1
        
    sum += int(nums[0] + nums[len(nums) - 1])
    
print("Sum:", sum)
