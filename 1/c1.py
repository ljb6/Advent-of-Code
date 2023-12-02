input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

lista = input.split('\n')

sum = 0

for line in lista:
    
    nums = []
    
    for i in line:
        try:
            test = int(i)
            nums.append(i)
        except:
            pass
            
    sum += int(nums[0] + nums[len(nums) - 1])
    
print("Sum:", sum)
