#algoritmo trasformata
def rotazione(parola):
    matrice=[]
    i = 0
    j = 0
    for carattere in parola:
        matrice.append(parola[i:]+parola[:j])  
        j = j+1
        i = i+1
    return matrice
def ordinamento(matrice):
    x = 0
    for stringa in matrice:
        y = 0
        for stringa in matrice:
            if matrice[x] < matrice[y]:
                    matrice[x], matrice[y] = matrice[y], matrice[x]
            y = y + 1        
        x = x + 1
    return matrice     
def codifica(matrice):
    z = 0
    codiceBWT=[]
    for stringa in matrice:
        codiceBWT.append(matrice[z][len(matrice[z]) - 1:])
        z = z + 1
    return codiceBWT
    
     
parola = input("inserisci la parola da codificare: ").lower()
codificaBWT = rotazione(parola)
print("-------------")
print (codificaBWT)
print("-------------")
codificaBWT = ordinamento(codificaBWT)
print("-------------")
print (codificaBWT)
print("-------------")
codificaBWT = codifica(codificaBWT)
print("-------------")
print (codificaBWT)
print("-------------")






