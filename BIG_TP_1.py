import math
print("===========================\nBienvenue dans le BIG TP1\n\n")

# Lecture des la source 1
Source_1 = []
Proba_1 = []
N = int(input ("Entrer le nombre de symboles de la source 1 : "))

print("\nsymboles source 1 : ")
firstTime = True
sommeProba = 0
while sommeProba != 100:
    if  firstTime:
        firstTime = False
    else:
        print("\nLa somme des probabilités doit être égale à 100%\nSymboles source 1 : ")
    sommeProba = 0
    Source_1 = []
    Proba_1 = []
    for i in range(0, N):
        symb = "x" + str(i+1)
        toAdd = int(input(symb + " : "))
        Proba_1.append(toAdd)
        Source_1.append(symb)
        sommeProba += toAdd


# Calcule de la quantité d'information de chaque symbole
# Fonction pour calcule de la quantité d'information
def QuantitéInformation(Proba):
    I = []
    for i in range(0, len(Proba)):
        I.append(round(-math.log2(Proba[i]/100), 3))
    return I

# Affichage de la quantité d'information
print("\nLa quantité d'information chaque symbole (Source 1) : ")
I = QuantitéInformation(Proba_1)
for i in range(0, N):
    print("I(" + str(Source_1[i]) + ") = " + str(I[i]))
        

