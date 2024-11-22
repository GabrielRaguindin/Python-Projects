#Imported Modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

root = Tk()
root.title("Photo Editor Application")
root.geometry("640x690")
root.configure(background="gray25")

#Functions
def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_canvas(event):
    global lasx, lasy
    if draw_combo.get() == "Red":
       canvas2.create_line((lasx, lasy, event.x, event.y), fill='red3', width=4)
    elif draw_combo.get() == "Blue":
       canvas2.create_line((lasx, lasy, event.x, event.y), fill='dodger blue', width=4)
    elif draw_combo.get() == "Green":
       canvas2.create_line((lasx, lasy, event.x, event.y), fill='chartreuse2', width=4)
    lasx, lasy = event.x, event.y

def delete():
    canvas2.delete("all")

def select_photo():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image=img1                                                                                                                                                                                                                

def blur(event):
    global img_path, img1, imgg
    for m in range(0, v1.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg) 
        canvas2.create_image(300, 210, image=img1)
        canvas2.image=img1

def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Brightness(img)
        img2 = imgg.enhance(m)
        img3 = ImageTk.PhotoImage(img2)
        canvas2.create_image(300, 210, image=img3)
        canvas2.image=img3

def sharpness(event):
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Sharpness(img)
        img4 = imgg.enhance(m)
        img5 = ImageTk.PhotoImage(img4)
        canvas2.create_image(300, 210, image=img5)
        canvas2.image=img5

def contrast(event):
    global img_path, img6, img7
    for m in range(0, v4.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(img)
        img6 = imgg.enhance(m)
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(300, 210, image=img7)
        canvas2.image=img7
            
def saturation(event):
    global img_path, img8, img9
    for m in range(0, v5.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Color(img)
        img8 = imgg.enhance(m)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(300, 210, image=img9)
        canvas2.image=img9
            
def rotate_photo(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = img.rotate(int(rotate_combo.get()))
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image=img11
        
def flip_photo(event):
    global img_path, img12, img13
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if flip_combo.get() == "FLIP(Left to Right)":
       img12 = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_combo.get() == "FLIP(Top to Bottom)":
       img12 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img13 = ImageTk.PhotoImage(img12)
    canvas2.create_image(300, 210, image=img13)
    canvas2.image=img13   

def insert_border(event):
    global img_path, img14, img15
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img14 = ImageOps.expand(img, border=int(border_combo.get()), fill=10)
    img15 = ImageTk.PhotoImage(img14)
    canvas2.create_image(300, 210, image=img15)
    canvas2.image=img15  

img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None
img13 = None
img15 = None

def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("JPG file","*.jpg")])
    if file: 
       if canvas2.image==img1:
          imgg.save(file)
       elif canvas2.image==img3:
          img2.save(file)
       elif canvas2.image==img5:
          img4.save(file)
       elif canvas2.image==img7:
          img6.save(file)
       elif canvas2.image==img9:
          img8.save(file)
       elif canvas2.image==img11:
          img10.save(file)
       elif canvas2.image==img13:
          img12.save(file)
       elif canvas2.image==img15:
          img14.save(file)

def dev_team():
    messagebox.showinfo("Development Team:", " Gabriel Raguindin ")

#Tkinter GUI Layout(Labels, Scales, Combos)
blurr = Label(root, text="Blur", bg="gray25", fg="ghost white", font=("Calibri 20 italic"), width=9, anchor='e')
blurr.place(x=10, y=3)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, length=120, orient=HORIZONTAL, command=blur)
scale1.place(x=150, y=10)

bright = Label(root, text="Brightness", bg="gray25", fg="ghost white", font=("Calibri 20 italic"))
bright.place(x=20, y=48)
v2 = IntVar()   
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, length=120, orient=HORIZONTAL, command=brightness) 
scale2.place(x=150, y=55)

sharp = Label(root, text="Sharpness", bg="gray25", fg="ghost white", font=("Calibri 20 italic"))
sharp.place(x=21, y=92)
v3 = IntVar()   
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3, length=120, orient=HORIZONTAL, command=sharpness) 
scale3.place(x=150, y=100)

contr = Label(root, text="Contrast", bg="gray25", fg="ghost white", font=("Calibri 20 italic"))
contr.place(x=39, y=136)
v4 = IntVar()
scale4 = ttk.Scale(root, from_=0, to=10, variable=v4, length=120, orient=HORIZONTAL, command=contrast)
scale4.place(x=150, y=145)

color = Label(root, text="Saturation", bg="gray25", fg="ghost white", font=("Calibri 20 italic"))
color.place(x=330, y=3)
v5 = IntVar()
scale5 = ttk.Scale(root, from_=0, to=10, variable=v5, length=120, orient=HORIZONTAL, command=saturation)
scale5.place(x=460, y=10)

flip = Label(root, text="Flip Photo", bg="gray25", fg="ghost white", font=("Calibri 19 italic"))
flip.place(x=343, y=45)
values1 = ["FLIP(Left to Right)", "FLIP(Top to Bottom)"]
flip_combo = ttk.Combobox(root, values=values1, font=('Calibri 10 italic'))
flip_combo.place(x=460, y=53)
flip_combo.bind("<<ComboboxSelected>>", flip_photo)

border = Label(root, text="Insert Border", bg="gray25", fg="ghost white", font=("Calibri 19 italic"))
border.place(x=310, y=79)
values2 = [i for i in range(10, 45, 5)]
border_combo = ttk.Combobox(root, values=values2, font=("Calibri 10 italic"))
border_combo.place(x=460, y=88)
border_combo.bind("<<ComboboxSelected>>", insert_border)

rotate = Label(root, text="Rotate Photo", bg="gray25", fg="ghost white", font=("Calibri 19 italic"))
rotate.place(x=310, y=113)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=('Calibri 10 italic'))
rotate_combo.place(x=460, y=122)
rotate_combo.bind("<<ComboboxSelected>>", rotate_photo)

drawing = Label(root, text="Draw", bg="gray25", fg="ghost white", font="Calibri 19 italic")
drawing.place(x=389, y=144)
values3 = ["Red", "Blue", "Green",]
draw_combo = ttk.Combobox(root, values=values3, font=("Calibri 10 italic"))
draw_combo.place(x=460, y=154)
draw_combo.bind("<<ComboboxSelected>>", draw_canvas)

#Canvas
canvas2 = Canvas(root, width="600", bg='white smoke', height="430", relief=SUNKEN, bd=3)
canvas2.place(x=15, y=185)
canvas2.bind("<Button-1>", get_x_and_y)
canvas2.bind("<B1-Motion>", draw_canvas)

#Buttons
btn1 = Button(root, text="Select Photo", bg='deepskyblue2', fg='ghost white', bd=3, font=('Calibri 15 italic'), relief=RAISED, command=select_photo)
btn1.place(x=50, y=601)
btn2 = Button(root, text="Save", width=12, bg='deepskyblue2', fg='ghost white', bd=3, font=('Calibri 15 italic'), relief=RAISED, command=save)
btn2.place(x=179, y=601)
btn3 = Button(root, text="Exit", width=12, bg='red3', fg='black', bd=3, font=('Calibri 15 italic'), relief=RAISED, command=root.destroy)
btn3.place(x=460, y=601)
btn4 = Button(root, text="Delete", width=12, bg='red3', fg='black', bd=3, font=('Calibri 15 italic'), relief=RAISED, command=delete)
btn4.place(x=320, y=601)
btn5 = Button(root, text="Development Team", bg='gray10', fg='ghost white', padx=160, pady=5, bd=3, font=('FixedSys 15'), relief=RAISED, command=dev_team)
btn5.place(x=88, y=649)

root.mainloop()
