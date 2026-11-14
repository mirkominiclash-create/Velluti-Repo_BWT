#algoritmo trasformata
parola = "banana$"
lettera = ""
matrice=[]
i = 0
j = 0

for carattere in parola:
    matrice.append(parola[i:]+parola[:j])
    
    j = j+1
    i = i+1
print (matrice)
x = 0

for stringa in matrice:
    y = 0
    for stringa in matrice:
        if matrice[x] < matrice[y]:
                matrice[x], matrice[y] = matrice[y], matrice[x]
        y = y + 1        
    x = x + 1

print(matrice)    




