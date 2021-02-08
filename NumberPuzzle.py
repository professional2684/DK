from numpy.core.defchararray import isnumeric
import time
import multiprocessing
import concurrent.futures as cf 

def createList(lstNum, inpNum):

    if isnumeric(str(inpNum)):
        if inpNum == 0:
            print('no numbers')
            return 'No Numbers'
        elif inpNum//10 == 0:
            lstNum.append(inpNum)
            return lstNum
        else:
            lstNum.append(inpNum%10)
            inpNum = inpNum//10
            createList(lstNum, inpNum)
    else:
        return 'Please enter numbers!'
    return lstNum

def calcGuess(lstNum):
    slayer = ''

    PossibleList = []
    
    for num in lstNum:
        slayer += str(num)

    layers = slayer[1:] + slayer[:1]
    if 3 * int(slayer) == int(layers):
        return '{} is correct guess'.format(slayer)
    return '{} is incorrect guess'.format(slayer)


def calcPossible():
    PossibleList = []
    
    for x in range(1000000, 9999999):
        if 3 * x == int(str(x)[1:]+str(x)[:1]):
            PossibleList.append(x)
    print(PossibleList)


def calcPossibleNew(x):
    
    if 3 * x == int(str(x)[1:]+str(x)[:1]):
        return x
    
if __name__ == '__main__':
    inpNum = 142857
    result = createList([],inpNum)
    result.reverse()
    guess = calcGuess(result)
    print(guess)
    
    possibleList = []
    
    t1 = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map(calcPossibleNew, range(1000000, 9999999))
        print(result)

    t2 = time.time()
#     print(possibleList)
    print('time taken :', t2-t1)