listaNumrave = [1,2,3,4,5,6,7,8,9,10,11,12]


# for stupid in n:
#     print(stupid)  
#     for i in range(1,stupid+1):
#         fact = fact * i
#         print (fact)

def factoriel(numri):
    fact = 1
    for i in range(1,numri+1):
        fact = fact * i
    print (fact)
    
for numer in listaNumrave:
    factoriel(numer)