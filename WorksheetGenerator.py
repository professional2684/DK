import numpy as np

def decimalAddition():
    n = 1
    
#     with open('worksheet1.txt', 'w') as f:
#         strEq = str(np.random.choice(range(100)) / 100) +' + '+ str(np.random.choice(range(100)) / 100) + ' ='
#         f.write(strEq)
    
    with open('worksheet1.txt','w') as f:
        while n <= 48:
            if n % 4 == 0:
                separator = '\n\n\n'
            else:
                separator = '\t\t\t\t'
            strEq = str(np.random.choice(range(100)) / 100) +' + '+ str(np.random.choice(range(100)) / 100) + ' =' + separator
            f.write(strEq)
             
            n += 1
