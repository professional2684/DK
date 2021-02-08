import random
import time

# numList = []
# finalList = []
# 
# for n in range(50):
#     finalList.append(random.choice(range(1,100)))
# 
# uniqueList = list(set(finalList))
# finalList.sort()

uniqueList = [2, 4, 5, 6, 14, 17, 18, 22, 24, 26, 27, 29, 31, 32, 33, 37, 38, 39, 42, 44, 47, 50, 51, 52, 56, 60, 62, 63, 66, 69, 71, 72, 74, 76, 78, 79, 81, 82, 84, 89, 90, 93, 95]

print(uniqueList.__contains__(2))


count = 0
# print(13 //2)

def binary_serach(data, inpNum):
    low = 0
    high = len(data)-1    
    mid = (low+ high) // 2
    
    if inpNum == data[mid]:
        return True
    
    elif inpNum < data[mid]:
        high = mid - 1
    else:
        low = mid + 1
    return False


def linear_search(data, inpNum):
    for n in data:
        if inpNum == n:
            return True
        
    return False

def binary_search_recursive(data, inpNum, low, high):

    mid = (low+ high) // 2

    if low > high:
        return False
    
    if inpNum == data[mid]:
        return True
    
    elif inpNum < data[mid]:
        return binary_search_recursive(data, inpNum, low, mid - 1)
        
    else:
        return binary_search_recursive(data, inpNum, mid + 1, high)
        
    return False

print(uniqueList)
inpNum = 19

# t1 = time.time()*1000000000000000000000000
print(binary_search_recursive(uniqueList, inpNum, 0, len(uniqueList)-1))
# t2 = time.time()*1000000000000000000000000
# print('Binary Execution : ',t2-t1)
# 
# 
# t1 = time.time()*1000000000000000000000000
# print(linear_search(uniqueList, inpNum))
# t2 = time.time()*1000000000000000000000000
# print('Linear Execution : ',t2-t1)


# print(len(uniqueList))
# print(uniqueList[len(uniqueList)-1])


# print(len(finalList))
# print(finalList)


