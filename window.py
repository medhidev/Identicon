from tkinter import *
import main

root = Tk()
root.geometry("600x500")
root.resizable(False, False)

def run():
    main.main()

button = Button(root, text='Lancer le code', command=run())

root.mainloop()
