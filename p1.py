def liste_düzleştir(liste):
    liste = str(liste).replace("[", "").replace("]", "").split(",")
    k = list()
    for i in liste:
        i = i.strip(" ").replace("'", "")
        k.append(i)
    return k

def ters_cevir(liste):
    for i in range(len(liste)):
        liste[i] = liste[i][::-1]
    return liste[::-1]

y=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
x=[[1, 2], [3, 4], [5, 6, 7]]
x=ters_cevir(x)

print(liste_düzleştir(y))
print(x)
