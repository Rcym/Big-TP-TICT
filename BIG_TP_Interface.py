from tkinter import *
from tkinter import ttk
import math

# Fonction pour calculer l'entropie d'une source
def Entropie(Proba):
    H = 0
    for i in range(0, len(Proba)):
        H += -Proba[i] * math.log2(Proba[i])
    return round(H, 3)

def QuantitéInformation(Proba):
    I = []
    for i in range(0, len(Proba)):
        I.append(round(-math.log2(Proba[i]), 3))
    return I

def EntropieConjointe(Proba_xy):
    Hxy = 0
    for i in range(0, len(Proba_xy)):
        for j in range(0, len(Proba_xy[i])):
            Hxy += -(Proba_xy[i][j]) * math.log2(Proba_xy[i][j])
    return round(Hxy, 3)

# Fonction pour calculer la quantité d'information mutuelle
def QuantitéInfoMutuelle(Proba1, Proba2):
    Ixy = []
    for i in range(0, len(Proba1)):
        Ixy.append([])
        for j in range(0, len(Proba2)):
            Ixy[i].append(round(-math.log2((Proba1[i])*(Proba2[j])), 3))
    return

# Function pour calculer l'entropie conditionnelle
def EntropieConditionnelle(PX, P_YSX, YXorXY):
    if YXorXY == "YsX":
        Hcond = 0
        for i in range(0, len(PX)):
            for j in range(0, len(P_YSX[i])):
                Hcond += -(PX[i]) * (P_YSX[j][i]) * math.log2(P_YSX[j][i])
        return round(Hcond, 3)
    elif YXorXY == "XsY":
        Hcond = 0
        for i in range(0, len(PX)):
            for j in range(0, len(P_YSX[i])):
                Hcond += -(PX[i]) * (P_YSX[i][j]) * math.log2(P_YSX[i][j])
        return round(Hcond, 3)

def ProbaCond(Pxy, Px, N1, N2, direction):
    if direction == "ysx":
        Proba_YsX = []
        for i in range(0, N1):
            Pysx_In = []
            for j in range(0, N2):
                Inside = Pxy[i][j] / Px[i]
                Inside = round(Inside, 3)
                Pysx_In.append(Inside)
            Proba_YsX.append(Pysx_In)
        return Proba_YsX
    elif direction == "xsy":
        Proba_YsX = []
        for i in range(0, N1):
            Pysx_In = []
            for j in range(0, N2):
                Inside = Pxy[i][j] / Px[j]
                Inside = round(Inside, 3)
                Pysx_In.append(Inside)
            Proba_YsX.append(Pysx_In)
        return Proba_YsX

def QinformationMutuelle(Pxy, Px, Py):
    Ixy2 = 0
    for i in range(0, len(Px)):
        for j in range(0, len(Py)):
            Ixy2 += (Pxy[i][j]) * math.log2((Pxy[i][j])/((Px[i])*(Py[j])))
    return round(Ixy2, 3)

def erreurPopup(currentWindow):
    errWindow = Toplevel(currentWindow)
    errWindow.configure(bg="red")
    Label(errWindow, text="Une erreur lors de la saisie des donnes veuillez reesayer", font=("Arial", 14)).pack(padx=8,pady=8)
    return

    
root = Tk()
root.title("BIG TP Interface")
root.geometry("500x500")
root.resizable(width=False, height=False)
root["bg"] = "#333"


Titre = Label(root, text="BIG TP Interface", font=("Arial", 24), padx=20, pady=10)
Titre.pack()
Titre.configure(bg="#444", fg="#fff")


def showPrefix():

    def showInputPrefix():
        try :
            taille = int(taillePrompt_input.get())
        except:
            errWindow = Toplevel(prefixWindow)
            errWindow.configure(bg="#333")
            Label(errWindow, text="Une erreur lors de la saisie des donnes veillez reesayer").pack(padx=10,pady=10)
            return

        # haut du tableau (Labels)
        sourceInputPrefix_PRE = Frame(prefixWindow, padx=10, pady=3)
        sourceInputPrefix_PRE.configure(bg="#222")
        sourceInputPrefix_PRE.pack(pady=5)

        Symb_text = Label(sourceInputPrefix_PRE, text="Symbol", font=("Arial", 12), padx=5)
        Symb_text.configure(bg="#222", fg="#fff")
        Code_text = Label(sourceInputPrefix_PRE, text="|  Code  |", font=("Arial", 12), padx=5)
        Code_text.configure(bg="#222", fg="#fff")
        Proba_text = Label(sourceInputPrefix_PRE, text="Probabilité", font=("Arial", 12), padx=5)
        Proba_text.configure(bg="#222", fg="#fff")

        Symb_text.grid(row=0, column=0)
        Code_text.grid(row=0, column=1)
        Proba_text.grid(row=0, column=2)



        # Corp de la l'input source
        wrapper1 = LabelFrame(prefixWindow, height=100)
        wrapper1.configure(bg="#333")
        wrapper1.pack(fill="y", expand="no")

        theCanvas = Canvas(wrapper1)
        theCanvas.configure(bg="#222")
        theCanvas.pack(side=LEFT)

        yscrollbar = ttk.Scrollbar(wrapper1, orient=VERTICAL, command=theCanvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)

        theCanvas.configure(yscrollcommand=yscrollbar.set)
        theCanvas.bind("<Configure>", lambda e: theCanvas.configure(scrollregion=theCanvas.bbox("all")))
        theCanvas.bind_all("<MouseWheel>", lambda event: theCanvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        theFrame = Frame(theCanvas)
        theFrame.configure(bg="#222")
        theCanvas.create_window((0,0), window=theFrame, anchor="nw")
        theCanvas.configure(width=210, bg="#222")

        inputs = []
        for i in range(0, taille):
            Symb = Label(theFrame, text="X" + str(i+1) + " : ", font=("Arial", 12), pady=5)
            Symb.configure(bg="#222", fg="#fff")
            Symb.grid(row=i, column=0)

            Code = Entry(theFrame, font=("Arial", 12), width=10)
            Code.grid(row=i, column=1)

            Space = Label(theFrame, text="   ", font=("Arial", 12))
            Space.configure(bg="#222")
            Space.grid(row=i, column=2)
            
            Proba = Entry(theFrame, font=("Arial", 12), width=5)
            Proba.grid(row=i, column=3)
        
            inputs.append([Symb, Code, Proba])




        def findPrefix() :
            # getting input array
            Codes = []
            Probas = []

            # verification inputs
            sommeProba = 0
            for elem in inputs:
                Proba = float(elem[2].get())
                Code = elem[1].get()
                for lettre in Code:
                    if not ((lettre == "0") or (lettre == "1")):
                        errWindow = Toplevel(prefixWindow)
                        errWindow.configure(bg="red")
                        Label(errWindow, text="les codes ne doivent contenire que des 0 et des 1").pack(padx=10, pady=10)
                        return

                Codes.append(elem[1].get())
                Probas.append(Proba)
                sommeProba += Proba
            print(sommeProba)
            if sommeProba != 1:
                errWindow = Toplevel(prefixWindow)
                errWindow.configure(bg="red")
                Label(errWindow, text="La somme des probabilitées doit étre égale a 1").pack(padx=10, pady=10)
                return
            
            # verification prefix
            isPrefix = True
            for i in range(len(Codes)):
                for j in range(len(Codes)):
                    if (i != j) and Codes[i].startswith(Codes[j]):
                        isPrefix = False
                        break
            if isPrefix:
                print("Le code est un préfix")
                resultWindow = Toplevel(prefixWindow)
                resultWindow.configure(bg="green")
                Result = Label(resultWindow, text="Le code est un code préfix", font=("Arial",20), padx=10, pady=10)
                Result.pack(padx=10, pady=10)

            else:
                print("Le code n'es pas un code préfix")
                resultWindow = Toplevel(prefixWindow)
                resultWindow.configure(bg="red")
                Result = Label(resultWindow, text="Le code n'est pas un code préfix", font=("Arial",20), padx=10, pady=10)
                Result.pack(padx=10, pady=10)

            
            




        # Bouton valider
        sourceInputPrefix_validate = Button(prefixWindow, text="Valider", font=("Arial", 12), command=findPrefix)
        sourceInputPrefix_validate.configure(bg="#111", fg="#fff")
        sourceInputPrefix_validate.pack(pady=5)



    
    prefixWindow = Toplevel(root)
    prefixWindow.geometry("500x550")
    prefixWindow.configure(bg="#333")
    prefixWindow.resizable(False,False)
    prefixWindow.title("Préfix")


    Titre = Label(prefixWindow, text="BIG TP Interface", font=("Arial", 24), padx=20, pady=10)
    Titre.pack()
    Titre.configure(bg="#444", fg="#fff")


    # Prompt taille de la source
    taillePrompt = Frame(prefixWindow, padx=20, pady=20)
    taillePrompt.pack(pady=20)
    taillePrompt.configure(bg="#222")

    taillePrompt_text = Label(taillePrompt, text="Taille de la source : ", font=("Arial", 12))
    taillePrompt_text.configure(bg="#222", fg="#fff")
    taillePrompt_text.grid(row=0, column=0)

    taillePrompt_input = Entry(taillePrompt, font=("Arial", 12), width=10)
    taillePrompt_input.grid(row=0, column=1)

    taillePrompt_space = Label(taillePrompt, text="   ", font=("Arial", 12))
    taillePrompt_space.configure(bg="#222")
    taillePrompt_space.grid(row=0, column=2)

    taillePrompt_button = Button(taillePrompt, text=">", font=("Arial", 12), padx=5, pady=2, command=showInputPrefix)
    taillePrompt_button.configure(bg="#111", fg="#fff")
    taillePrompt_button.grid(row=0, column=3)










def show_BIG_TP1():
    Pxy = []
    tailleSource_1 = 0
    tailleSource_2 = 0

    def enterPxy():
        try:
            global tailleSource_1
            global tailleSource_2
            tailleSource_1 = int(entrySource1.get())
            tailleSource_2 = int(entrySource2.get())
        except:
            errWindow = Toplevel(entryWindow)
            errWindow.configure(bg="red")
            Label(errWindow, text="Une erreur lors de la saisie des donnes veuillez reesayer", font=("Arial", 14)).pack(padx=8,pady=8)
            return
        entryWindow.geometry("800x600")



        # Showing scalable entry fields for Pxy
        wrapper1 = LabelFrame(entryWindow)
        wrapper1.configure(bg="#333")
        wrapper1.pack(fill="y", expand="no")

        theCanvas = Canvas(wrapper1)
        theCanvas.configure(bg="#222")
        #theCanvas.pack()
        theCanvas.grid(row=0, column=0)

        yscrollbar = ttk.Scrollbar(wrapper1, orient=VERTICAL, command=theCanvas.yview)
        #yscrollbar.pack(side=RIGHT, fill=Y)
        yscrollbar.grid(row=0,column=1, sticky=NS)
        xscrollbar = ttk.Scrollbar(wrapper1, orient=HORIZONTAL, command=theCanvas.xview)
        #xscrollbar.pack(side=BOTTOM, fill=X)#, expand="yes")
        xscrollbar.grid(row=1, column=0, sticky=EW)

        theCanvas.configure(yscrollcommand=yscrollbar.set)
        theCanvas.bind("<Configure>", lambda e: theCanvas.configure(scrollregion=theCanvas.bbox("all")))
        theCanvas.bind_all("<MouseWheel>", lambda event: theCanvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # Taille fenétre dynamique
        #taille_x = 83 * tailleSource_1
        #taille_y = 34 * tailleSource_2
        #if taille_x > 600: taille_x = 600
        #if taille_y > 400: taille_y = 400

        #if tailleSource_1 <=4: taille_x = 200
        #if tailleSource_2 <=4: taille_x = 200


        theFrame = Frame(theCanvas)
        theFrame.configure(bg="#222")
        theCanvas.create_window((0,0), window=theFrame, anchor="nw")
        #theCanvas.configure(width=taille_x, height=taille_y, bg="#222")             # <-- size canvas
        theCanvas.configure(width=600, height=400, bg="#222")             # <-- size canvas

        # preparing table entry
        for i in range(tailleSource_2):
            #th = Label(theFrame, text="P(xi,y" + str(i+1) + ")", font=("Arial",14), bg="#444", fg="#fff")
            th = Label(theFrame, text="y" + str(i+1), font=("Arial",14), bg="#444", fg="#fff")
            th.grid(row=0, column=i+1, sticky=NSEW)
        for j in range(tailleSource_1):
            #th = Label(theFrame, text="P(x" + str(j+1) + ",yj)", font=("Arial",14), bg="#444", fg="#fff")
            th = Label(theFrame, text="x" + str(j+1), font=("Arial",14), bg="#444", fg="#fff")
            th.grid(row=j+1, column=0, sticky=NSEW)

        for i in range(tailleSource_1):
            laColonne = []
            for j in range(tailleSource_2):
                td = Entry(theFrame)
                td.configure(font=("Arial", 12), width=5)
                td.grid(row=i+1, column=j+1, padx=2)
                laColonne.append(td)
            Pxy.append(laColonne)

        # Affichage de point 0,0 du tableau (P(x,y))
        Label(theFrame, text="P(x,y)", font=("Arial",16), bg="#444", fg="#fff").grid(row=0, column=0)


        # Adding valider button on top
        space2 = Label(entryFrame_plusBtn, text="   ", bg="#333")
        space2.grid(row=0, column=4)
        validateBTN = Button(entryFrame_plusBtn, text="Valider P(x,y)", font=("Arial",16), padx=5, pady=10, bg="#222", fg="#fff", command=validerPxy)
        validateBTN.grid(row=0, column=5)
            

    def validerPxy():
        # Verification matrice entré
        global tailleSource_1
        global tailleSource_2
        
        sommePxy = 0
        for i in range(tailleSource_1):
            for j in range(tailleSource_2):
                try:
                    sommePxy += float(Pxy[i][j].get())
                except:
                    erreurPopup(entryWindow)
                    return
        if sommePxy != 1:
            errWindow = Toplevel(entryWindow)
            errWindow.configure(bg="red")
            Label(errWindow, text="La somme des probabilité doit étre égale a 1", font=("Arial", 14)).pack(padx=8,pady=8)
            return
        
        # Transforming Pxy into values instead of using .get()
        for i in range(tailleSource_1):
            for j in range(tailleSource_2):
                Pxy[i][j] = float(Pxy[i][j].get())
        print(Pxy)
        
        # Calcul Px et Py
        Px = []
        Py = []
        for i in range(tailleSource_1):
            Px_temp = 0
            for j in range(tailleSource_2):
                Px_temp += Pxy[i][j]
            Px.append(round(Px_temp,2))
        for i in range(tailleSource_2):
            Py_temp = 0
            for j in range(tailleSource_1):
                Py_temp += Pxy[j][i]
            Py.append(round(Py_temp,2))

        ## Calcule de TOUT
        global Pxsy
        global Pysx
        global Hx
        global Hy
        global Hxy
        global Ixy
        global Ixy_H
        global Hysx
        global Hxsy
        global Ix
        global Iy
        global Hysx_H
        global Hxsy_H


        Pysx = ProbaCond(Pxy, Px, tailleSource_1, tailleSource_2, "ysx")
        Pxsy = ProbaCond(Pxy, Py, tailleSource_1, tailleSource_2, "xsy")
        Hx = Entropie(Px)
        Hy = Entropie(Py)
        Hxy = EntropieConjointe(Pxy)
        Hysx = EntropieConditionnelle(Px, Pysx, "YsX")
        Hxsy = EntropieConditionnelle(Py, Pxsy, "XsY")

        Ixy_H = round((Hx + Hy - Hxy), 3)
        Ixy = QinformationMutuelle(Pxy, Px, Py)

        Ix = QuantitéInformation(Px)
        Iy = QuantitéInformation(Py)
        
        Hxsy_H = Hxy - Hx     # hnaaaa
        Hysx_H = Hxy - Hy

        # Creating Display Window TP1
        entryWindow.destroy()
        displayWindow = Toplevel(root)
        displayWindow.geometry("1000x600")
        displayWindow.resizable(False,False)
        displayWindow.configure(bg="#333")
        
        def switchToX():
            X_btn.configure(bg="#fff", fg="#333")
            Y_btn.configure(bg="#333", fg="#fff")
            isXselected = True
            displaySource("toX")
        def switchToY():
            X_btn.configure(bg="#333", fg="#fff")
            Y_btn.configure(bg="#fff", fg="#333")
            isXselected = False
            displaySource("toY")

        # Sources display section
        sourceDisplay = LabelFrame(displayWindow, bg="#222", width=200, height=600)
        sourceDisplay.pack(side=RIGHT, fill=Y)
        Label(sourceDisplay, text="  Sources :  ", font=("Arial",20), bg="#222", fg="#fff").pack(pady=10)
        btnFrame_source = Frame(sourceDisplay, bg="#222")
        btnFrame_source.pack()
        X_btn = Button(btnFrame_source,text="Source X", bg="#fff", fg="#333", bd=3, font="bold", command=switchToX)
        Y_btn = Button(btnFrame_source,text="Source Y", bg="#333", fg="#fff", bd=3, font="bold", command=switchToY)
        X_btn.grid(row=0, column=0, padx=4)
        Y_btn.grid(row=0, column=1, padx=4)
        Label(sourceDisplay, text=" ", font=("Arial",24), bg="#222").pack(pady=2)

        def displaySource(toWhere):
            if toWhere == "" or toWhere == "toX":
                isXselected = True
            else:
                isXselected = False

            tailleToUse = tailleSource_1 if isXselected else tailleSource_2
            symbToUse = "X" if isXselected else "Y"
            P = Px if isXselected else Py

            global rapper
            global Qinfo_frame
            try:
                rapper.destroy()
                Qinfo_frame.destroy()
            except:
                pass

            ################################### scroll bar section
            rapper = LabelFrame(sourceDisplay, height=100)
            rapper.configure(bg="#333")
            rapper.pack(fill="y", expand="no")

            theCanvas = Canvas(rapper)
            theCanvas.configure(bg="#222")
            theCanvas.pack(side=LEFT)

            yscrollbar = ttk.Scrollbar(rapper, orient=VERTICAL, command=theCanvas.yview)
            yscrollbar.pack(side=RIGHT, fill=Y)

            theCanvas.configure(yscrollcommand=yscrollbar.set)
            theCanvas.bind("<Configure>", lambda e: theCanvas.configure(scrollregion=theCanvas.bbox("all")))
            theCanvas.bind_all("<MouseWheel>", lambda event: theCanvas.yview_scroll(int(-1*(event.delta/120)), "units"))

            theFrame = Frame(theCanvas)
            theFrame.configure(bg="#222")
            theCanvas.create_window((0,0), window=theFrame, anchor="nw")
            theCanvas.configure(width=210, bg="#222")
            ################################### end of scroll bar section


            for i in range(tailleToUse):
                toWrite = "P(" + symbToUse + str(i) + ") = " + str(P[i])
                addedLabel = Label(theFrame, text=toWrite, bg="#222", fg="#fff", font=("Arial",16)).pack(padx=20, pady=5)
            
            Qinfo_frame = Frame(sourceDisplay, bg="#222")
            Label(Qinfo_frame, text="Entropie :      ", bg="#222", fg="#fff", font=("Arial",16)).pack()
            labelAntropie_text = "H(" + symbToUse + ") = " + str(Entropie(P))
            labelEntropie = Label(Qinfo_frame, text=labelAntropie_text, bg="#222", fg="#fff", font=("Arial",16))
            labelEntropie.pack()
            Qinfo_frame.pack(pady=10)

        displaySource("")


        # Genral display
        generalDisplay = Frame(displayWindow, bg="#333")
        generalDisplay.pack(side=RIGHT, fill=BOTH, expand=YES)
        generalButtonFrame = Label(generalDisplay, bg="#444")
        generalButtonFrame.pack(side=TOP, fill=X, pady=10)

        # general buttons
        Qinfo_btn = Button(generalButtonFrame, text="Quantité d'information", font=("Arial",18), bg="#fff", fg="#333", bd=3, command=lambda: generalChange("Qinfo"))
        Proba_btn = Button(generalButtonFrame, text="Probabilitées", font=("Arial",18), bg="#333", fg="#fff", bd=3, command=lambda: generalChange("Proba"))
        Entropie_btn = Button(generalButtonFrame, text="Entropie", font=("Arial",18), bg="#333", fg="#fff", bd=3, command=lambda: generalChange("Entropie"))

        Qinfo_btn.grid(row=0, column=0, padx=5)
        Proba_btn.grid(row=0, column=1, padx=5)
        Entropie_btn.grid(row=0, column=2, padx=5)

        global generalMainFrame
        generalMainFrame = Frame(generalDisplay, bg="#333")
        generalMainFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)

        def generalChange(btn):
            try:
                global generalMainFrame
                generalMainFrame.destroy()
                generalMainFrame = Frame(generalDisplay, bg="#333")
                generalMainFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
            except:
                pass


            if btn == "Qinfo":
                Qinfo_btn.configure(bg="#fff", fg="#333")
                Proba_btn.configure(bg="#333", fg="#fff")
                Entropie_btn.configure(bg="#333", fg="#fff")

                def showQinfoo(Source):
                    QinfoWindoww = Toplevel(displayWindow)
                    QinfoWindoww.title("I("+ Source +")")
                    QinfoWindoww.geometry("200x500")
                    QinfoWindoww.resizable(False,False)
                    QinfoWindoww.configure(bg="#333")

                    ################################### scroll bar section
                    IxIyWrapper = LabelFrame(QinfoWindoww, height=400)
                    IxIyWrapper.configure(bg="#333")
                    IxIyWrapper.pack(fill="y", expand="no", pady=20)

                    theCanvas = Canvas(IxIyWrapper)
                    theCanvas.configure(bg="#222")
                    theCanvas.pack(side=LEFT)

                    yscrollbar = ttk.Scrollbar(IxIyWrapper, orient=VERTICAL, command=theCanvas.yview)
                    yscrollbar.pack(side=RIGHT, fill=Y)

                    theCanvas.configure(yscrollcommand=yscrollbar.set)
                    theCanvas.bind("<Configure>", lambda e: theCanvas.configure(scrollregion=theCanvas.bbox("all")))
                    theCanvas.bind_all("<MouseWheel>", lambda event: theCanvas.yview_scroll(int(-1*(event.delta/120)), "units"))

                    IxIyframe = Frame(theCanvas)
                    IxIyframe.configure(bg="#222")
                    theCanvas.create_window((0,0), window=IxIyframe, anchor="nw")
                    theCanvas.configure(width=600,height=400 , bg="#222")
                    ################################### end of scroll bar section

                    if Source == "X":
                        tailleSource = tailleSource_1
                        symbToUse = "x"
                        I = Ix
                    else:
                        tailleSource = tailleSource_2
                        symbToUse = "y"
                        I = Iy
                    
                    for i in range(tailleSource):
                        Label(IxIyframe, text="I(" + symbToUse + str(i) + ") = " + str(I[i]), font=("Arial", 18), bg="#222", fg="#fff").grid(row=i, column=0, pady=5, padx=20)

                Label(generalMainFrame, text="Calcule de la quantité d'information :", font=("Arial 22 bold underline"), bg="#333", fg="#fff", justify=LEFT).pack(fill=X,padx=10, pady=10)
                PxPyContainer = Frame(generalMainFrame, bg="#333")
                PxPyContainer.pack(fill=X, padx=10)
                Label(PxPyContainer, text="Quantité d'information des sources X et Y :", font=("Arial",16), bg="#333", fg="#fff").grid(row=0, column=0, sticky=W)
                Button(PxPyContainer, text="I(xi)", bg="#333", fg="#fff", bd=3, padx=5, pady=5, font=("Arial",16), command=lambda: showQinfoo("X")).grid(row=0, column=1, padx=5)
                Button(PxPyContainer, text="I(yj)", bg="#333", fg="#fff", bd=3, padx=5, pady=5, font=("Arial",16), command=lambda: showQinfoo("Y")).grid(row=0, column=2, padx=5)

                PxyContainer = Frame(generalMainFrame, bg="#333")
                PxyContainer.pack(fill=X, padx=5, pady=40)
                Label(PxyContainer, text=" ", bg="#333").grid(row=0, column=0, padx=10, sticky=W) # espace

                Label(PxyContainer, text="Calcule de la quantité d'information mutuelle :", font=("Arial 18 bold underline"), bg="#333", fg="#fff", justify=LEFT).grid(row=1, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="Methode 1 :", font=("Arial 18 bold"), bg="#333", fg="#fff", justify=LEFT).grid(row=2, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="On utilise la formule : I(x,y) = P(x,y) * log2(P(x,y) / (P(x) * P(y)))", font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=3, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="===> I(X,Y) = "+str(Ixy), font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=4, column=0, padx=10, sticky=W)

                Label(PxyContainer, text=" ", bg="#333").grid(row=5, column=0, padx=10, sticky=W) # espace
                
                Label(PxyContainer, text="Methode 2 :", font=("Arial 18 bold"), bg="#333", fg="#fff", justify=LEFT).grid(row=6, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="On utilise la formule de l'entropie : I(X,Y) = H(X) + H(Y) - H(X,Y)", font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=7, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="===> I(X,Y) = "+str(Ixy_H), font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=8, column=0, padx=10, sticky=W)





            elif btn == "Proba":
                Qinfo_btn.configure(bg="#333", fg="#fff")
                Proba_btn.configure(bg="#fff", fg="#333")
                Entropie_btn.configure(bg="#333", fg="#fff")

                secondGeneralBtnFrame = Frame(generalMainFrame, bg="#444")
                secondGeneralBtnFrame.pack(pady=15, fill=X)

                # Proba buttons
                Pxy_btn = Button(secondGeneralBtnFrame, text="P(x,y)", font=("Arial",16), bg="#fff", fg="#333", bd=3, command=lambda: probaChange("Pxy"))
                Pxsy_btn = Button(secondGeneralBtnFrame, text="P(x/y)", font=("Arial",16), bg="#333", fg="#fff", bd=3, command=lambda: probaChange("Pxsy"))
                Pysx_btn = Button(secondGeneralBtnFrame, text="P(y/x)", font=("Arial",16), bg="#333", fg="#fff", bd=3, command=lambda: probaChange("Pysx"))

                Pxy_btn.grid(row=0, column=0, padx=5)
                Pxsy_btn.grid(row=0, column=1, padx=5)
                Pysx_btn.grid(row=0, column=2, padx=5)

                

                def probaChange(btn):
                    global probaScrol
                    try:
                        probaScrol.destroy()
                    except:
                        pass
                    ################################### scroll bar section
                    probaScrol = LabelFrame(generalMainFrame, height=400)
                    probaScrol.configure(bg="#333")
                    probaScrol.pack(fill="y", expand="no", pady=20)

                    theCanvas = Canvas(probaScrol)
                    theCanvas.configure(bg="#222")
                    theCanvas.pack(side=LEFT)

                    yscrollbar = ttk.Scrollbar(probaScrol, orient=VERTICAL, command=theCanvas.yview)
                    yscrollbar.pack(side=RIGHT, fill=Y)

                    theCanvas.configure(yscrollcommand=yscrollbar.set)
                    theCanvas.bind("<Configure>", lambda e: theCanvas.configure(scrollregion=theCanvas.bbox("all")))
                    theCanvas.bind_all("<MouseWheel>", lambda event: theCanvas.yview_scroll(int(-1*(event.delta/120)), "units"))

                    thePxyFrame = Frame(theCanvas)
                    thePxyFrame.configure(bg="#222")
                    theCanvas.create_window((0,0), window=thePxyFrame, anchor="nw")
                    theCanvas.configure(width=600,height=400 , bg="#222")
                    ################################### end of scroll bar section

                    # preparting the table
                    for i in range(tailleSource_2):
                        th = Label(thePxyFrame, text="y" + str(i+1), font=("Arial",14), bg="#444", fg="#fff")
                        th.grid(row=0, column=i+1, sticky=NSEW)
                    for j in range(tailleSource_1):
                        th = Label(thePxyFrame, text="x" + str(j+1), font=("Arial",14), bg="#444", fg="#fff")
                        th.grid(row=j+1, column=0, sticky=NSEW)

                    if btn == "Pxy":
                        Pxy_btn.configure(bg="#fff", fg="#333")
                        Pxsy_btn.configure(bg="#333", fg="#fff")
                        Pysx_btn.configure(bg="#333", fg="#fff")

                        # top left corder (title)
                        th = Label(thePxyFrame, text="P(x,y)", font=("Arial 14 bold"), bg="#444", fg="#fff")
                        th.grid(row=0, column=0, sticky=NSEW)

                        for i in range(tailleSource_1):
                            for j in range(tailleSource_2):
                                toWrite = str(Pxy[i][j])
                                Label(thePxyFrame, text=toWrite, font=("Arial",12,), bg="#222", fg="#fff").grid(row=i+1,column=j+1, padx=5, pady=6)

                    elif btn == "Pxsy":
                        Pxy_btn.configure(bg="#333", fg="#fff")
                        Pxsy_btn.configure(bg="#fff", fg="#333")
                        Pysx_btn.configure(bg="#333", fg="#fff")

                        # top left corder (title)
                        th = Label(thePxyFrame, text="P(x/y)", font=("Arial 14 bold"), bg="#444", fg="#fff")
                        th.grid(row=0, column=0, sticky=NSEW)

                        for i in range(tailleSource_1):
                            for j in range(tailleSource_2):
                                toWrite = str(Pxsy[i][j])
                                Label(thePxyFrame, text=toWrite, font=("Arial",12,), bg="#222", fg="#fff").grid(row=i+1,column=j+1, padx=5, pady=6)

                    elif btn == "Pysx":
                        Pxy_btn.configure(bg="#333", fg="#fff")
                        Pxsy_btn.configure(bg="#333", fg="#fff")
                        Pysx_btn.configure(bg="#fff", fg="#333")

                        # top left corder (title)
                        th = Label(thePxyFrame, text="P(y/x)", font=("Arial 14 bold"), bg="#444", fg="#fff")
                        th.grid(row=0, column=0, sticky=NSEW)


                        for i in range(tailleSource_1):
                            for j in range(tailleSource_2):
                                toWrite = str(Pysx[i][j])
                                Label(thePxyFrame, text=toWrite, font=("Arial",12,), bg="#222", fg="#fff").grid(row=i+1,column=j+1, padx=5, pady=6)

                probaChange("Pxy")

            elif btn == "Entropie":
                Qinfo_btn.configure(bg="#333", fg="#fff")
                Proba_btn.configure(bg="#333", fg="#fff")
                Entropie_btn.configure(bg="#fff", fg="#333")

                Label(generalMainFrame, text="Calcule de L'entropie :", font=("Arial 22 bold underline"), bg="#333", fg="#fff", justify=LEFT).pack(fill=X,padx=10, pady=10)
                PxPyContainer = Frame(generalMainFrame, bg="#333")
                PxPyContainer.pack(fill=X, padx=10)
                Label(PxPyContainer, text="Entropie des sources X et Y :", font=("Arial",16), bg="#333", fg="#fff").grid(row=0, column=0, sticky=W)
                Label(PxPyContainer, text="H(X) = "+ str(Hx) + "   |   H(Y) = " + str(Hy), bg="#333", fg="#fff", padx=5, pady=5, font=("Arial",16)).grid(row=1, column=0, padx=0)
                Label(PxPyContainer, text="H(X,Y) = " + str(Hxy), bg="#333", fg="#fff", padx=5, pady=5, font=("Arial",16)).grid(row=2, column=0, padx=0)

                PxyContainer = Frame(generalMainFrame, bg="#333")
                PxyContainer.pack(fill=X, padx=5, pady=20)
                Label(PxyContainer, text=" ", bg="#333").grid(row=0, column=0, padx=10, sticky=W) # espace

                Label(PxyContainer, text="Calcule des entropies Conditionnelles :", font=("Arial 18 bold underline"), bg="#333", fg="#fff", justify=LEFT).grid(row=1, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="Methode 1 :", font=("Arial 18 bold"), bg="#333", fg="#fff", justify=LEFT).grid(row=2, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="On utilise la formule : H(X/Y) = somme(P(xi) .somme(P(y/w).log(1/P(y/x))))", font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=3, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="===> H(X/Y) = "+str(Hxsy) + "(bits/symboles)", font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=4, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="===> H(Y/X) = "+str(Hysx) + "(bits/symboles)", font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=5, column=0, padx=10, sticky=W)

                Label(PxyContainer, text=" ", bg="#333").grid(row=6, column=0, padx=10, sticky=W) # espace
                
                Label(PxyContainer, text="Methode 2 :", font=("Arial 18 bold"), bg="#333", fg="#fff", justify=LEFT).grid(row=7, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="On utilise la formule de l'entropie : H(Y/X) = H(X,Y) - H(X)", font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=8, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="===> H(Y/X) = "+str(Hysx_H) + "(bits/symboles)", font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=9, column=0, padx=10, sticky=W)
                Label(PxyContainer, text="===> H(X/Y) = "+str(Hxsy_H) + "(bits/symboles)", font=("Arial 16"), bg="#333", fg="#fff", justify=LEFT).grid(row=10, column=0, padx=10, sticky=W)




            







    entryWindow = Toplevel(root)
    entryWindow.geometry("500x180")
    entryWindow.configure(bg="#333")
    entryWindow.resizable(False,False)
    entryWindow.title("BIG TP 1")

    Titre = Label(entryWindow, text="BIG TP 1 Interface", font=("Arial", 24), padx=20, pady=10)
    Titre.pack()
    Titre.configure(bg="#444", fg="#fff")

    # Frame containing size of Source1 and Source2
    entryFrame_plusBtn = Frame(entryWindow)
    entryFrame_plusBtn.configure(bg="#333")
    entryFrame_plusBtn.pack(pady=10)

    # button validate
    buttonValidate = Button(entryFrame_plusBtn, text=">", font=("Arial", 18), bg="#222", fg="#fff", padx=10, pady=10, command=enterPxy)
    buttonValidate.grid(row=0, column=2)
    
    space = Label(entryFrame_plusBtn, text="      ")
    space.configure(bg="#333")
    space.grid(row=0, column=1)

    # Actual entry frame
    entryFrame = LabelFrame(entryFrame_plusBtn)
    entryFrame.configure(bg="#333")
    entryFrame.grid(row=0, column=0)

    entrySource1_frame = Frame(entryFrame)
    entrySource1_frame.configure(bg="#222", padx=8)
    text1 = Label(entrySource1_frame, text="Taille de la source 1 : ", font=("Arial", 16))
    text1.configure(bg="#222", fg="white", padx=0, pady=5)
    entrySource1 = Entry(entrySource1_frame, font=("Arial",16), width=5)
    text1.grid(row=0, column=0)
    entrySource1.grid(row=0, column=1)
    entrySource1_frame.grid(row=0, column=0)

    entrySource2_frame = Frame(entryFrame)
    entrySource2_frame.configure(bg="#222", padx=8)
    text2 = Label(entrySource2_frame, text="Taille de la source 2 : ", font=("Arial", 16))
    text2.configure(bg="#222", fg="white", padx=0, pady=5)
    entrySource2 = Entry(entrySource2_frame, font=("Arial",16), width=5)
    text2.grid(row=0, column=0)
    entrySource2.grid(row=0, column=1)
    entrySource2_frame.grid(row=1, column=0)



    


    


menuElement2 = Button(root, text="BIG TP 1", font=("Arial", 12), width=20, height=3, command=show_BIG_TP1).pack(pady=30)
menuElement3 = Button(root, text="BIG TP 2", font=("Arial", 12), width=20, height=3).pack(pady=30)
menuElement3 = Button(root, text="Préfix", font=("Arial", 12), width=20, height=3, command=showPrefix).pack(pady=30)


root.mainloop()