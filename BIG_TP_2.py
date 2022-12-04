print("===========================\nBienvenue dans le BIG TP1\n\n")

N = int(input("donnez la taille de votre source : "))
print("\n")

Source = []
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
        toAdd = int(input("x" + str(i) + " : "))
        sommeProba += toAdd
        Source.append(toAdd)
print(Source)