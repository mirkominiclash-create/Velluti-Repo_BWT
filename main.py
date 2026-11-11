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
