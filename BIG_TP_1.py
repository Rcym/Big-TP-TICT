import math
print("===========================\nBienvenue dans le BIG TP1\n\n")


#Proba_x = [10, 20, 70]           # Source X
Proba_x = [30, 70]
N = len(Proba_x)
Source_1 = []
print("Source 1 :")
for i in range(0, N):
    Source_1.append("x" + str(i+1))
    print(Source_1[i] + "(" + str(i+1) + ") = " + str(Proba_x[i]) + " %")

#Proba_y = [10, 90]               # Source Y
Proba_y = [40, 60]
N2 = len(Proba_y)
Source_2 = []
print("\nSource 2 :")
for i in range(0, N2):
    Source_2.append("y" + str(i+1))
    print(Source_2[i] + "(" + str(i+1) + ") = " + str(Proba_y[i]) + " %")

Proba_xy = []   # Source XY
Nxy = len(Proba_xy)
sommePxy = 0
# affichage de la probabilité conjointe
if Nxy != 0:
    print("\nLa probabilité conjointe P(x,y) : ")
    for i in range(0, N):
        for j in range(0, N2):
            symb = "(x" + str(i+1) + ",y" + str(j+1) + ')'
            print("P" + symb + " = " + str(Proba_xy[i][j]) + " %")
            sommePxy += Proba_xy[i][j]
    print("somme = " + str(sommePxy) + " %")





## Fonctions
# Fonction pour calcule de la quantité d'information
def QuantitéInformation(Proba):
    I = []
    for i in range(0, len(Proba)):
        I.append(round(-math.log2(Proba[i]/100), 3))
    return I

# Fonction pour calculer l'entropie d'une source
def Entropie(Proba):
    H = 0
    for i in range(0, len(Proba)):
        H += -Proba[i]/100 * math.log2(Proba[i]/100)
    return round(H, 3)

def EntropieConjointe(Proba_xy):
    Hxy = 0
    for i in range(0, len(Proba_xy)):
        for j in range(0, len(Proba_xy[i])):
            Hxy += -(Proba_xy[i][j]/100) * math.log2(Proba_xy[i][j]/100)
    return round(Hxy, 3)

# Fonction pour calculer la quantité d'information mutuelle
def QuantitéInfoMutuelle(Proba1, Proba2):
    Ixy = []
    for i in range(0, len(Proba1)):
        Ixy.append([])
        for j in range(0, len(Proba2)):
            Ixy[i].append(round(-math.log2((Proba1[i]/100)*(Proba2[j]/100)), 3))
    return I

# Function pour calculer l'entropie conditionnelle
def EntropieConditionnelle(PX, P_YSX, YXorXY):
    if YXorXY == "YsX":
        Hcond = 0
        for i in range(0, len(PX)):
            for j in range(0, len(P_YSX[i])):
                Hcond += -(PX[i]/100) * (P_YSX[j][i]) * math.log2(P_YSX[j][i])
        return round(Hcond, 3)
    elif YXorXY == "XsY":
        Hcond = 0
        for i in range(0, len(PX)):
            for j in range(0, len(P_YSX[i])):
                Hcond += -(PX[i]/100) * (P_YSX[i][j]) * math.log2(P_YSX[i][j])
        return round(Hcond, 3)

print("\n\n===========================\n\n")







# Lecture des la source 1
if N == 0 :
    Source_1 = []
    Proba_x = []
    N = int(input ("Entrer le nombre de symboles de la source 1 : "))

    print("symboles source 1 : ")
    firstTime = True
    sommeProba = 0
    while sommeProba != 100:
        if  firstTime:
            firstTime = False
        else:
            print("\nLa somme des probabilités doit être égale à 100%\nSymboles source 1 : ")
        sommeProba = 0
        Source_1 = []
        Proba_x = []
        for i in range(0, N):
            symb = "y" + str(i+1)
            toAdd = int(input(symb + " : "))
            Proba_x.append(toAdd)
            Source_1.append(symb)
            sommeProba += toAdd


# Calcule et affichage de la quantité d'information (Source 1)
print("\nLa quantité d'information chaque symbole (Source 1) : ")
I = QuantitéInformation(Proba_x)
for i in range(0, N):
    print("I(" + str(Source_1[i]) + ") = " + str(I[i]))
        

# Calcule et affichage de l'entropie de la source 1
H = Entropie(Proba_x)
print("\nL'entropie de la source 1 est : \nH(X) = " + str(H) + " (bits/symbole)")



print("\n")



# Lecture des la source 2
if N2 == 0 :
    Source_2 = []
    Proba_y = []
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
        Source_2 = []
        Proba_y = []
        for i in range(0, N2):
            symb = "x" + str(i+1)
            toAdd = int(input(symb + " : "))
            Proba_y.append(toAdd)
            Source_2.append(symb)
            sommeProba += toAdd

# Calcule et affichage de la quantité d'information (Source 2)
print("La quantité d'information chaque symbole (Source 2) : ")
I2 = QuantitéInformation(Proba_y)
for i in range(0, N2):
    print("I(" + str(Source_2[i]) + ") = " + str(I2[i]))

# Calcule et affichage de l'entropie de la source 2
H2 = Entropie(Proba_y)
print("\nL'entropie de la source 2 est : \nH(Y) = " + str(H2) + " (bits/symbole)")



print("\n\n===========================\n\n")










## Nouvelles sources a partire de P(x,y) + Entropie avec 2 facons
# Saisie de la probabilité conjointe
if Nxy == 0 :
    print("La probabilité conjointe P(x,y) : ")
    firstTime = True
    sommePxy = 0
    while sommePxy != 100:
        if firstTime:
            firstTime = False
        else:
            print("\nLa somme des probabilités doit être égale à 100%\n")
        Proba_xy = []
        sommePxy = 0
        for i in range(0, N):
            Proba_xyy = []
            for j in range(0, N2):
                symb = "(x" + str(i+1) + ",y" + str(j+1) + ')'
                pxyy = int(input("P" + symb + " : "))
                Proba_xyy.append(pxyy)
                sommePxy += pxyy
            Proba_xy.append(Proba_xyy)

# Calcule et affichage de P(x) et P(y) a partire de P(x,y)
print("\nOn fait sortire les P(xi) et P(yj) a partire de P(xi,yj) :\nOn utilise la relation : P(xI) = Somme(P(xI,yj))\n")

# Calcule de P(x)
Proba_x = []
for i in range(0, N):
    Px = 0
    for j in range(0, N2):
        Px += Proba_xy[i][j]
    Proba_x.append(Px)

# Calcule de P(y)
Proba_y = []
for i in range(0, N2):
    Py = 0
    for j in range(0, N):
        Py += Proba_xy[j][i]
    Proba_y.append(Py)
    

# Affichage de P(x)
for i in range(0, N):
    print("P(x" + str(i+1) +") : " + str(Proba_x[i]) + " %")
Hx = Entropie(Proba_x)
print("===> H(X) = " + str(Hx) + " (bits/symbole)")

print("\n")

# Affichage de P(y)
for i in range(0, N2):
    print("P(y" + str(i+1) +") : " + str(Proba_y[i]) + " %")
Hy = Entropie(Proba_y)
print("===> H(Y) = " + str(Hy) + " (bits/symbole)")
    
# Calcule et affichage de l'entropie conjointe (H(X,Y))
Hxy = EntropieConjointe(Proba_xy)
print("\n=====> H(X,Y) = " + str(Hxy) + " (bits/symbole)")




print("\n")
print("On sait que H(X,Y) = H(X) + H(Y) - I(X,Y)")
print("==> I(X,Y) = H(X) + H(Y) - H(X,Y)")
Ixy = round((Hx + Hy - Hxy), 3)
print("==> I(X,Y) = " + str(Ixy) + " (bits/symbole)")

print("\nOu alors on peut calculer I(x,y) en utilisant la formule : I(x,y) = P(x,y) * log2(P(x,y) / (P(x) * P(y)))")
Ixy2 = 0
for i in range(0, N):
    for j in range(0, N2):
        Ixy2 += (Proba_xy[i][j]/100) * math.log2((Proba_xy[i][j]/100)/((Proba_x[i]/100)*(Proba_y[j]/100)))
Ixy2 = round(Ixy2, 3)
print("===> I(X,Y) = " + str(Ixy2) + " (bits/symbole)")





print("\n\n===========================\n\n")




## Calcule des probabilitées conditionnelles
# Calcule de P(y/x)
print("On calcule les probabilités conditionnelles P(y/x) :\nOn utilise la formule de Bayes : P(y/x) = P(x,y) / P(x)\n")
Proba_YsX = []
for i in range(0, N):
    Pysx_In = []
    for j in range(0, N2):
        Inside = Proba_xy[i][j] / Proba_x[i]
        Inside = round(Inside, 3)
        Pysx_In.append(Inside)
    Proba_YsX.append(Pysx_In)

# Affichage de P(y/x)
for i in range(0, N):
    for j in range(0, N2):
        print("P(y" + str(j+1) + "/x" + str(i+1) + ") : " + str(Proba_YsX[i][j]))

print("\n")

# Calcule de P(x/y)
print("On calcule les probabilités conditionnelles P(x/y) :\nOn utilise la formule de Bayes : P(x/y) = P(x,y) / P(y)\n")
Proba_XsY = []
for i in range(0, N):
    Pxsy_In = []
    for j in range(0, N2):
        Inside = Proba_xy[i][j] / Proba_y[j]
        Inside = round(Inside, 3)
        Pxsy_In.append(Inside)
    Proba_XsY.append(Pxsy_In)

# Affichage de P(x/y)
for i in range(0, N):
    for j in range(0, N2):
        print("P(x" + str(i+1) + "/y" + str(j+1) + ") : " + str(Proba_XsY[i][j]))




print("\n\n===========================\n\n")



## Calcule des entropies conditionnelles
# Calcule de H(y/x)
print("On calcule les entropies conditionnelles H(y/x) :\nOn utilise la formule : H(y/x) = somme(Px * somme(P(y/x) * log2(P(y/x))))\n")
H_YsX = EntropieConditionnelle(Proba_x, Proba_YsX, "YsX")
H_XsY = EntropieConditionnelle(Proba_y, Proba_XsY, "XsY")
print("===> H(Y/X) = " + str(H_YsX) + " (bits/symbole)")
print("===> H(X/Y) = " + str(H_XsY) + " (bits/symbole)")

print("\nOn peut vérifier ces résultats en utilisant l'autre formule :")
print("H(Y/X) = H(X,Y) - H(X) => H(Y/X)\nH(Y/X) = " + str(Hxy) + " - " + str(Hx) + "\nH(Y/X) = " + str(round((Hxy - Hx), 3)) + " (bits/symbole)\n")
print("H(X/Y) = H(X,Y) - H(Y) => H(X/Y)\nH(X/Y) = " + str(Hxy) + " - " + str(Hy) + "\nH(X/Y) = " + str(round((Hxy - Hy), 3)) + " (bits/symbole)")

