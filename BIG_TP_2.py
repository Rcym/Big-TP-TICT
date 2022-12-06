print("===========================\nBienvenue dans le BIG TP1\n\n")

N = int(input("donnez la taille de votre source : "))
print("\n")

Source = []
Symb = []
sommeProba = 0
firstTime = True
while (sommeProba != 100):
    if firstTime:
        firstTime = False
    else :
        print("\nLa somme des probabilité doit étre égale a 100 %")
    Source = []
    sommeProba = 0
    for i in range(0,N):
        symb = "x" + str(i+1)
        toAdd = int(input(symb + " : "))
        sommeProba += toAdd
        Source.append(toAdd)
        Symb.append(symb)

# créaction du tableau de la source
Data = []
for i in range(0,N):
    symbole = []
    symbole.append(Symb[i])
    symbole.append(Source[i])
    symbole.append("")
    symbole.append([])
    symbole.append([])
    Data.append(symbole)

# Copying Data
Source_DATA = []
for i in range(0,N):
    Source_DATA.append(Data[i].copy())


for i in range(0,2):
    ## HuffMan
    # sort
    Data.sort(key=lambda x: x[1], reverse=True)

    # adding last 2 to new one
    haut = Data[-2]
    bas = Data[-1]

    ProbaHaut = haut[1]
    ProbaBas = bas[1]
    newProba = ProbaHaut + ProbaBas

    newSymb = ["", newProba, bas, haut]
    print("new symb :")
    print(newSymb)
    print("\n")

    Data.pop()
    Data.pop()
    Data.append(newSymb)


    print("\n\n AFFICHAGE :")
    # affichage successif
    print(Data)


# Lecture de "l'arbre"



    