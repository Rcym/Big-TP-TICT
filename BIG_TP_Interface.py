from tkinter import *

root = Tk()
root.title("BIG TP Interface")
root.geometry("500x500")
root.resizable(width=False, height=False)
root["bg"] = "#333"


Titre = Label(root, text="BIG TP Interface", font=("Arial", 24), padx=20, pady=10)
Titre.pack()
Titre.configure(bg="#444", fg="#fff")

menuElement1 = Button(root, text="BIG TP 1", font=("Arial", 12))
menuElement2 = Button(root, text="BIG TP 1", font=("Arial", 12)).pack(pady=20)
menuElement3 = Button(root, text="BIG TP 1", font=("Arial", 12)).pack(pady=20)


root.mainloop()