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
    symbole.append([])
    symbole.append([])
    Data.append(symbole)


# Copying Data
Source_DATA = []
for i in range(0,N):
    Source_DATA.append(Data[i].copy())

# Huffman coding
while (len(Data) != 1):
    ## HuffMan
    # sort
    Data.sort(key=lambda x: x[1], reverse=True)

    # adding last 2 to new one
    haut = Data[-2]
    bas = Data[-1]
    ProbaHaut = haut[1]
    ProbaBas = bas[1]
    newProba = ProbaHaut + ProbaBas

    # Crating new symbol
    newSymb = ["", newProba, bas, haut]

    Data.pop()
    Data.pop()
    Data.append(newSymb)
    Data.sort(key=lambda x: x[1], reverse=True)


# Lecture de "l'arbre"
Result = []
def LectureArbre(arbre, codeAccumule):
    if arbre[0] != "":
        resultElement = []
        resultElement.append(arbre[0])
        resultElement.append(codeAccumule)
        Result.append(resultElement)
    else:
        LectureArbre(arbre[2], codeAccumule + "0")
        LectureArbre(arbre[3], codeAccumule + "1")

# Lecture de l'arbre
LectureArbre(Data[0], "")
Result.sort(key=lambda x: x[0])

# Affichage des résultats
print("\nLe codage en utilisant l'algorithm de Huffman :\n")
for i in range(0,N):
    print(Result[i][0] + " -> " + Result[i][1])


# Calcul de la longueur moyenne
LongeurMoyenne = 0
for i in range(0,N):
    LongeurMoyenne += len(Result[i][1])
LongeurMoyenne /= N
print("\nLa longueur moyenne est de : " + str(LongeurMoyenne) + " bits")

# Calcule de l'entropie de la source
import math
Entropie = 0
for i in range(0,N):
    Entropie += Source[i]/100 * math.log2(100/Source[i])
print("\nL'entropie de la source est de : " + str(Entropie) + " bits")

# Calcule de l'efficacité du codage
Efficacite = Entropie/LongeurMoyenne
print("\nL'efficacité du codage est de : " + str(Efficacite))


    