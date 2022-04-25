def sum(numratEZgjedhur):
    rezultati = 0
    if type(numratEZgjedhur) != type([]):
        return "Tipi i te dhenes eshte i gabuar"
    for numrat in numratEZgjedhur:
        rezultati += numrat
    return(rezultati)

# NON LIST CASE
numriDy = 2
rezultatuINumritDy = sum(numriDy)
print(rezultatuINumritDy)


# LIST CASE

lista = [1,2,3]
rezultatiIListes = sum(lista)
print(rezultatiIListes)