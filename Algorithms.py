vowels = 'aeiou'

testString = 'the'


def vowel_count(inpString):
    vowelCount = 0
    
    for i in inpString:
        if (i.lower() in vowels and i.isalpha()):
            vowelCount +=1
    
    return vowelCount

def vowel_count_recursive(inpString):
   
    if inpString == '':
        return 0

    for i in inpString:
        if (i.lower() in vowels and i.isalpha()):
            return 1 + vowel_count_recursive(inpString[1:])
        else:
            return vowel_count_recursive(inpString[1:])

def vowel_count_recursive_variable(inpString, count):
   
    if inpString == '':
        print('inside if :',inpString)
#         count = 0
        
    else:

        for i in inpString:
            if (i.lower() in vowels and i.isalpha()):
                count = count +1
                return vowel_count_recursive(inpString[1:], count)
            else:
                return vowel_count_recursive(inpString[1:], count)
    
    return count

# print(vowel_count(testString))
# print(vowel_count_recursive(testString))


import math
# Q = Square root of [(2 * C * D)/H]

def calculate_formula(inpNumLst):
    C = 50
    H = 30
    calcList = []
    
    if len(inpNumLst) == 0:
        return inpNumLst 
    
    for num in inpNumLst:
        calcList.append(int(math.sqrt((2 * C * num) / H)))
    return calcList

print(calculate_formula([10,20,30]))