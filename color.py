from tkinter import *

def change_color():
    # Trouvez l'index de l'élément sélectionné
    index = liste.curselection()
    
    # Si l'élément est sélectionné
    if index:
        # Changez la couleur d'arrière-plan de l'élément sélectionné en rouge
        liste.itemconfig(index, {'bg': 'red'})

root = Tk()
root.geometry("400x300")
root.resizable(False, False)

liste = Listbox(root)
index = liste.curselection()
liste.itemconfig(index, {'bg': 'red'})
liste.insert(1, "")
liste.insert(2, "test")
liste.insert(3, "Green")
liste.insert(4, "Yellow")
liste.insert(5, "Orange")
liste.insert(6, "Black")
liste.insert(7, "Blue")
liste.insert(8, "Red")
liste.insert(9, "Green")
liste.insert(10, "Yellow")
liste.insert(11, "Orange")
liste.insert(12, "Black")
liste.insert(13, "Blue")
liste.insert(14, "Red")
liste.insert(15, "Green")

liste.place(x=300, y=60)

root.mainloop()
