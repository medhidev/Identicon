from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from PIL import Image, ImageTk
# import main

# CONFIG
root = Tk()
background = "#7884FF"

root.geometry("500x500")
root.configure(bg=background)
root.title("Identicon Generator")
root.iconbitmap("images/logo.ico")
root.resizable(False, False)

# COMPONENTS
# Label
lenght_label = Label(root, text="LENGHT", bg=background)
lenght_label.place(x=40, y=40)

hight_label = Label(root, text="HIGHT", bg=background)
hight_label.place(x=40, y=80)

# Entry
lenght_entry = Entry(root, width=10, highlightthickness=1)
lenght_entry.config(highlightbackground = "black", highlightcolor= "black")
lenght_entry.place(x=100, y=40)

hight_entry = Entry(root, width=10, highlightthickness=1)
hight_entry.config(highlightbackground = "black", highlightcolor= "black")
hight_entry.place(x=100, y=80)

# Color
lenght_label = Label(root, text="COLOR", bg=background)
lenght_label.place(x=250, y=60)

# --------- Btn_color ----------

def color_choice():
    colors = askcolor(title="Color pannel")

#  RED
red = Button(root, text="     ", bg="red", activebackground="red")
red.configure(relief=SOLID, bd=2, highlightthickness=0)
red.place(x=310, y=40)

# ORANGE
orange = Button(root, text="     ", bg="orange", activebackground="orange")
orange.configure(relief=SOLID, bd=2, highlightthickness=0)
orange.place(x=332, y=40)

# YELLOW-ORANGE
yellange = Button(root, text="     ", bg="#FFD800", activebackground="#FFD800")
yellange.configure(relief=SOLID, bd=2, highlightthickness=0)
yellange.place(x=354, y=40)

# LIME
lime = Button(root, text="     ", bg="#B6FF00", activebackground="#B6FF00")
lime.configure(relief=SOLID, bd=2, highlightthickness=0)
lime.place(x=376, y=40)

# GREEN
green = Button(root, text="     ", bg="#4CFF00", activebackground="#4CFF00")
green.configure(relief=SOLID, bd=2, highlightthickness=0)
green.place(x=398, y=40)

# ----------------------------------

# LIGHT_GREEN
light_green = Button(root, text="     ", bg="#00FF21", activebackground="#00FF21")
light_green.configure(relief=SOLID, bd=2, highlightthickness=0)
light_green.place(x=310, y=62)

# CYAN
cyan = Button(root, text="     ", bg="#00FF90", activebackground="#00FF90")
cyan.configure(relief=SOLID, bd=2, highlightthickness=0)
cyan.place(x=332, y=62)

# LIGHT BLUE
light_blue = Button(root, text="     ", bg="#00FFFF", activebackground="#00FFFF")
light_blue.configure(relief=SOLID, bd=2, highlightthickness=0)
light_blue.place(x=354, y=62)

# BLUE
blue = Button(root, text="     ", bg="#0094FF", activebackground="#0094FF")
blue.configure(relief=SOLID, bd=2, highlightthickness=0)
blue.place(x=376, y=62)

 # DARK BLUE
dark_blue = Button(root, text="     ", bg="#0026FF", activebackground="#0026FF")
dark_blue.configure(relief=SOLID, bd=2, highlightthickness=0)
dark_blue.place(x=398, y=62)

# ----------------------------------

# LIGHT PURPLE
purple = Button(root, text="     ", bg="#B200FF", activebackground="#B200FF")
purple.configure(relief=SOLID, bd=2, highlightthickness=0)
purple.place(x=310, y=84)

# PINK
pink = Button(root, text="     ", bg="#FF7F7F", activebackground="#FF7F7F")
pink.configure(relief=SOLID, bd=2, highlightthickness=0)
pink.place(x=332, y=84)

# YELLOW
yellow = Button(root, text="     ", bg="#FFFF00", activebackground="#FFFF00")
yellow.configure(relief=SOLID, bd=2, highlightthickness=0)
yellow.place(x=354, y=84)

# BROWN
brown = Button(root, text="     ", bg="#7F3300", activebackground="#7F3300")
brown.configure(relief=SOLID, bd=2, highlightthickness=0)
brown.place(x=376, y=84)

# GRAY
gray = Button(root, text="     ", bg="#404040", activebackground="#404040")
gray.configure(relief=SOLID, bd=2, highlightthickness=0)
gray.place(x=398, y=84)

# CUSTOM
gray = Button(root, text="Custom", bg="#5984FF", activebackground="#5984FF", command=color_choice)
gray.configure(relief=SOLID, bd=2, highlightthickness=0)
gray.place(x=340, y=120)

# Rendu Identicon
image = ImageTk.PhotoImage(Image.open("identicon.png"))
preview = Label(image=image, width=300, height=300)
preview.place(x=20, y=150)

# bouton Refresh / Download

# refresh = Button(root, )
# refresh.place(20, y=150)

# download = Button()
# download.place(x=20, y=150)

root.mainloop()


