from tkinter import *
from tkinter import messagebox
import random

colours = ['red','blue','yellow','green','purple','orange','white','black','brown','pink']
score = 0
time = 30

def GameStart(event):
    if time==30:
       Timer()
    ColorPalette()
 
def ColorPalette():
    global score
    global time
    if time > 0:
       colour_entry.focus_set()
       if colour_entry.get().lower() == colours[1].lower():
          score += 1
          time += 2
       colour_entry.delete(0, END)
       random.shuffle(colours)
       colour.config(fg= str(colours[1]) , text = str(colours[0]))
       scoreLabel.config(text = "Score: " + str(score))
 
def Timer():
    global time
    if time > 0 :
       time -= 1
       timeLabel.config(text = "Time Remaining: "+ str(time))
       timeLabel.after(1000, Timer)
       if time == 0:
          if score >= 100:
             gameover = Label(root, text = "Game Over, damn fast hands", bg='gray50', fg='white', font = ('System', 12))
          elif score >= 60:
             gameover = Label(root, text = "Game Over, you're getting a hang of it", bg='gray50', fg='white', font = ('System', 12))
          elif score >= 40:
             gameover = Label(root, text = "Game Over, okay not bad", bg='gray50', fg='white', font = ('System', 12))
          elif score >= 20:
             gameover = Label(root, text = "Game Over, still not high enough", bg='gray50', fg='white', font = ('System', 12))
          elif score >= 10:
             gameover = Label(root, text = "Game Over, *yawn*", bg='gray50', fg='white', font = ('System', 12))
          elif score >= 0:
             gameover = Label(root, text = "Game Over, is that all you got?", bg='gray50', fg='white', font = ('System', 12))
          gameover.place(x=90, y=135)

def dev():
    messagebox.showinfo("CREDITS", "Developer: Gabriel Raguindin")
 
if __name__=='__main__':
 
    root = Tk()
    root.title('Word Color Game')
    root.geometry('375x200')
    root.configure(background="gray50")

    button = Button(root, text = "EXIT", bg='gray5', fg='red', bd=3, relief=RAISED, font = ('FixedSys', 12), command=root.destroy)
    button.place(x=320, y=165)

    button2 = Button(root, text = "CREDITS", bg='gray5', fg='white', bd=3, relief=RAISED, font = ('FixedSys', 12), command=dev)
    button2.place(x=10, y=165)

    instructions = Label(root, text = 'TYPE THE COLOR OF THE WORDS!\nPress "ENTER" to Start.', bg='gray50', fg='white', font = ('System', 12))
    instructions.place(x=75, y=35)
 
    scoreLabel = Label(root, text = 'Your Score: '+str(score), bg='gray25', fg='white', font=('System' , 12))
    scoreLabel.place(x=275, y=5)
 
    timeLabel = Label(root, text = 'Time Given: '+str(time), bg='gray25', fg='white', font=('System' , 12))
    timeLabel.place(x=10, y=5)
 
    colour = Label(root, bg='gray50', fg='white', font=('System',17))
    colour.place(x=145, y=70)
 
    colour_entry = Entry(root)
    colour_entry.focus_set()
    root.bind('<Return>',GameStart)
    colour_entry.place(x=130, y=115)
 
    root.mainloop()
