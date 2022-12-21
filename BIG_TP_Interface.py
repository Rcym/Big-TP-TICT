from tkinter import *
from tkinter import ttk

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








    


menuElement2 = Button(root, text="BIG TP 1", font=("Arial", 12), width=20, height=3).pack(pady=30)
menuElement3 = Button(root, text="BIG TP 2", font=("Arial", 12), width=20, height=3).pack(pady=30)
menuElement3 = Button(root, text="Préfix", font=("Arial", 12), width=20, height=3, command=showPrefix).pack(pady=30)


root.mainloop()