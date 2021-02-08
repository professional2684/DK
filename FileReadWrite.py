import csv
import pandas

i = 0

with open('Employee.csv') as csvFile:
    
    fileEmp = csv.reader(csvFile)
    for nm in fileEmp:
        for nm1 in nm:
            print(nm1,'\t',end='')
        print()
        i = i +1
        

print(i)

csvFile = pandas.read_csv('Employee.csv')

csvFile.rename(columns={"Name_Emp":"Name"}, inplace= True) # rename column labels
