from tkinter import *

root = Tk()
root.title("BIG TP Interface")
root.geometry("500x500")
root.resizable(width=False, height=False)
root["bg"] = "#333"


Titre = Label(root, text="BIG TP Interface", font=("Arial", 24), padx=20, pady=10)
Titre.pack()
Titre.configure(bg="#444", fg="#fff")

def showPrefix():
    prefixWindow = Toplevel(root)
    prefixWindow.title("TP Prefix")
    prefixWindow.geometry("500x500")
    prefixWindow.resizable(width=False, height=False)
    prefixWindow["bg"] = "#333"

    Titre = Label(prefixWindow, text="BIG TP Interface", font=("Arial", 24), padx=20, pady=10)
    Titre.pack()
    Titre.configure(bg="#444", fg="#fff")

    # ajout de la source
    


menuElement2 = Button(root, text="BIG TP 1", font=("Arial", 12), width=20, height=3).pack(pady=30)
menuElement3 = Button(root, text="BIG TP 2", font=("Arial", 12), width=20, height=3).pack(pady=30)
menuElement3 = Button(root, text="Préfix", font=("Arial", 12), width=20, height=3, command=showPrefix).pack(pady=30)


root.mainloop()