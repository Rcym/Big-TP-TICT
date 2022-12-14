from tkinter import *

root = Tk()
root.title("Entrainement tkinter")
root.geometry("400x560")
#root.resizable(width=False, height=False)
root["bg"] = "#333"

titre = Label(root, text="Application calculatrice", font=("Arial", 24), padx=20, pady=10)
titre.grid(row=0, column=0, columnspan=4)
titre.configure(bg="#444", fg="#fff")

current = [,,,]

def addNum(num):






# écrant
ecrantHaut = Label(root, text="b", font=("Arial", 12), padx=193, pady=7, bg="#555", justify="right").grid(row=1, column=0, columnspan=4)
ecrantBas = Label(root, text="a", font=("Arial", 12), padx=193, pady=15, bg="#777", justify="left").grid(row=2, column=0, columnspan=4)


# Création des boutons
btn1 = Button(root, text="1", font=("Arial", 12), width=10, height=5).grid(row=3, column=0)
btn2 = Button(root, text="2", font=("Arial", 12), width=10, height=5).grid(row=3, column=1)
btn3 = Button(root, text="3", font=("Arial", 12), width=10, height=5).grid(row=3, column=2)
btnAC = Button(root, text="AC", font=("Arial", 12), bg="#e28743", fg="white", width=10, height=5).grid(row=3, column=3)

btn4 = Button(root, text="4", font=("Arial", 12), width=10, height=5).grid(row=4, column=0)
btn5 = Button(root, text="5", font=("Arial", 12), width=10, height=5).grid(row=4, column=1)
btn6 = Button(root, text="6", font=("Arial", 12), width=10, height=5).grid(row=4, column=2)
btnPlus = Button(root, text="+", font=("Arial", 12),bg="#e28743", fg="white", width=10, height=5).grid(row=4, column=3)

btn7 = Button(root, text="7", font=("Arial", 12), width=10, height=5).grid(row=5, column=0)
btn8 = Button(root, text="8", font=("Arial", 12), width=10, height=5).grid(row=5, column=1)
btn9 = Button(root, text="9", font=("Arial", 12), width=10, height=5).grid(row=5, column=2)
btnMoins = Button(root, text="-", font=("Arial", 12), bg="#e28743", fg="white", width=10, height=5).grid(row=5, column=3)

btn0 = Button(root, text="0", font=("Arial", 12), width=10, height=5).grid(row=6, column=0)
btnVirgule = Button(root, text=",", font=("Arial", 12), width=10, height=5).grid(row=6, column=1)
btnEqual = Button(root, text="=", font=("Arial", 12), bg="#e28743", fg="white", width=21, height=5).grid(row=6, column=2, columnspan=2)


root.mainloop()