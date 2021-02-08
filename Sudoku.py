from pprint import pprint
import copy

def calcDistinctNumbers(numList):
    arrayNum = []
    
    for lst in numList:
        for num in lst:
            arrayNum.append(num)
    
    numList = list(set(arrayNum))

    return numList

def findCurrentRow(cell, listOfBox):
    curRows = []
    for boxItem in listOfBox:
        if cell in boxItem:
            for r in boxItem:
                curRows.append(r[0])
    return list(set(curRows))

def findCurrentCol(cell, listOfBox):
    curCols = []
    for boxItem in listOfBox:
        if cell in boxItem:
            for r in boxItem:
                curCols.append(r[1])
    return list(set(curCols))

def findUniqueKeyByValue(value, dictSet):
#     print(value, dictSet.values())
    sampleDict = {}
    for dictItem in dictSet:
        if value in dictSet[dictItem]:
#             sampleDict[dictItem] = 1
#             print(dictItem in sampleDict)
            if dictItem not in sampleDict:
                sampleDict[dictItem] = 1
            else:
                sampleDict[dictItem] += 1
#     print('sampleDict :',sampleDict)
    if len(sampleDict) == 1:
#         print('sampleDict :',sampleDict)
#         sampleDict = value
        return sampleDict
    else:
        return None
        

def findDistinctInrowcol(intermediateDict, listOfBox, callNo):
    
    listOfRow = [] # set of row elements
    listOfCol = [] # set of column elements
    disNumBox = []
    
    for rw in range(0,9):
        rowDict = {}
        colDict = {}
        
        for cl in range(0,9):
            if (cl, rw) in intermediateDict:
                colDict[(cl, rw)] = intermediateDict[(cl, rw)]
            if (rw, cl) in intermediateDict:
                rowDict[(rw, cl)] = intermediateDict[(rw, cl)]
        listOfCol.append(colDict)
        listOfRow.append(rowDict)
    
#     if callNo == 3:
#         for intVal in intermediateDict:
#             pass
#             print(intVal, intermediateDict[intVal])

    for boxItem in listOfBox:
        if (6, 1) in boxItem:
            for item in boxItem: # iterate each subgrid
                if item in intermediateDict:
                    disNumBox.append(intermediateDict[item])
            disNumBox = calcDistinctNumbers(disNumBox) # distinct numbers remaining in the sub grid
#             print(disNumBox)
            for biItem in boxItem:
                if biItem in intermediateDict:
                    print('biItem callNos: ',callNo, listOfCol[biItem[1]])
#                     print(item, intermediateDict[item])
    

    
    return intermediateDict


def findDistinctInSubGrid(missingDict, listOfBox):

    for box in listOfBox:
        dictValues = {}
        for item in box:
            
            if item in missingDict:
                for num in range(1,10):
                    if num in missingDict[item]:
                        if num in dictValues:
                            dictValues[num] += 1
                        else:
                            dictValues[num] = 1

        distinctNum = [dnum for dnum in dictValues if dictValues[dnum] == 1]

        for item in box:
            if item in missingDict:
                for num in distinctNum:
                    if num in missingDict[item]:
                        missingDict[item] = [num]
                        break
#     for item in box2:
#         if item in missingDict:
#             print(item, missingDict[item])
    return missingDict

def findMissing(numRange, callNo):
    tempRange = copy.deepcopy(numRange)
    
    if callNo < 4:
    
        findTheBlanks = []
        missingDict = {}
        distinctRow = []
        distinctCol = []
        numInRowGrid = {}
        numInColGrid = {}
        numList = [1,2,3,4,5,6,7,8,9]
        box1, box2, box3, box4, box5, box6, box7, box8, box9 = [],[],[],[],[],[],[],[],[]
        listOfBox = [box1, box2, box3, box4, box5, box6, box7, box8, box9] # set of subgrid
        
        for num1 in range(0,3):
            for num2 in range(0,3):
                box1.append((num1,num2))
                box2.append((num1,num2+3))
                box3.append((num1,num2+6))
                box4.append((num1+3,num2))
                box5.append((num1+3,num2+3))
                box6.append((num1+3,num2+6))
                box7.append((num1+6,num2))
                box8.append((num1+6,num2+3))
                box9.append((num1+6,num2+6))
#         print(listOfBox)
    #     find the cell with blanks
        for i, j in enumerate(numRange):
            for k in range(len(j)):
                if j[k] == '':
                    findTheBlanks.append((i,k))
    
        if len(findTheBlanks) != 0:
            for blankItem in findTheBlanks:
                rowList = []
                colList = []

                for numItem in range(0,9):
                    rowList.append(numRange[blankItem[0]][numItem])
                    colList.append(numRange[numItem][blankItem[1]])
                    
                missingFromRowList = [rnum for rnum in numList if rnum not in rowList]
                missingFromColList = [cnum for cnum in numList if cnum not in colList]
                possibleNum = [pnum for pnum in missingFromColList if pnum in missingFromRowList]
    
    #                 check for numbers within the subgrid 
                for boxItem in listOfBox:
                    if blankItem in boxItem:
                        for cell in boxItem:
                            cellValue = numRange[cell[0]][cell[1]]
    #                             print('cellValue: ',cellValue)
                            distinctRow.append(cell[0])
                            distinctCol.append(cell[1])
                            
                            if cellValue in possibleNum:
                                possibleNum.remove(cellValue)
                                
                        distinctRow = list(set(distinctRow))
                        distinctCol = list(set(distinctCol))
                       
    #                         iterate over the set of rows
                        for row in distinctRow:
                            numInRowGrid[row, blankItem[1]] = numRange[row][blankItem[1]]
                        for col in distinctCol:
                            numInColGrid[blankItem[0], col] = numRange[blankItem[0]][col]
                        
                missingDict[blankItem] = possibleNum

            intermediateDict = findDistinctInSubGrid(missingDict, listOfBox)
            tempSingle = []
            
            for intermediateCell in intermediateDict:
                if len(intermediateDict[intermediateCell]) == 1:
                    numRange[intermediateCell[0]][intermediateCell[1]] = intermediateDict[intermediateCell][0]
                    tempSingle.append(intermediateCell)
            
            for tmp in tempSingle:
                intermediateDict.pop(tmp)
#             if callNo == 6:
#                 pprint(listOfBox)

#             pprint(numRange)
            if tempRange == numRange:
                print('callNo :',callNo)
                result = findDistinctInrowcol(intermediateDict, listOfBox, callNo)
                print(result)
                for resultCell in result:
                    if len(result[resultCell]) == 1:
                        numRange[resultCell[0]][resultCell[1]] = result[resultCell][0]
                        tempSingle.append(resultCell)
              
                for tmp in tempSingle:
                    result.pop(tmp)
            
            callNo += 1
            findMissing(numRange, callNo)
        
#         print('finalDict :',finalDict)
            
    return numRange

if __name__ == '__main__':
    box1, box2, box3, box4, box5, box6, box7, box8, box9 = [],[],[],[],[],[],[],[],[]
    callNo = 0
#     numRange = [['',3,2,'','','','',5,7],
# [7,4,5,'',1,8,'','',6],
# [1,'','',7,'',3,2,8,''],
# [3,'',8,'','','',4,'',5],
# [4,'',9,1,'','','','',''],
# ['',6,1,'','',4,9,'',''],
# [2,5,7,6,'','','','',1],
# [9,8,'','',3,'',6,'',''],
# ['',1,'',8,'','','','',9]]
    numRange = [['',6,'','','','','',7,''],
['',1,'','',2,6,'','',''],
['','',4,'','','',2,5,''],
[9,'','','',5,'','','',3],
['','','','',8,'',9,'',''],
['',8,'','','','',4,'',7],
['','',6,4,'','','','',''],
['',4,'','','','','','',8],
['',9,'','',3,8,'','','']]

    numList = [1,2,3,4,5,6,7,8,9]
    result = findMissing(numRange, callNo)
    pprint(result)

# result = findUniqueKeyByValue(5, {(2, 1): [3, 7], (3, 1): [2, 7], (4, 1): [2, 3, 7], (6, 1): [2, 3, 5, 7]})
# pprint(result)