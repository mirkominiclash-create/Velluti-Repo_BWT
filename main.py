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


matrice2=[3,10,4,7]

for i in range (matrice2):
    for j in (0, len(matrice2)-i-1):
        if(matrice2[j]>matrice2[j+1]):
            matrice2[j],matrice2[j+1] = matrice2[j+1],matrice2[j]

print(matrice2)





