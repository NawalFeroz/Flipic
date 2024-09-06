import tkinter as tk
from tkinter import PhotoImage, messagebox
import pygame
import random


pygame.mixer.init() #for sounds


root = tk.Tk()
root.title("FLIPIC")
root.geometry('1500x1500')

bg = PhotoImage(file='backg.png')
playkey = PhotoImage(file='playbutton.png')
bg2 = bg.zoom(2, 2)


def play_click():
    pygame.mixer.music.load("2.mp3")
    pygame.mixer.music.play()

def play_but():
    pygame.mixer.music.load("22.mp3")
    pygame.mixer.music.play()

def play_succes():
    pygame.mixer.music.load("succes.mp3")
    pygame.mixer.music.play()

def play_screen():
    pygame.mixer.music.load("3.mp3")
    pygame.mixer.music.play()


def secondslide():
    root.withdraw()
    root2 = tk.Toplevel(root)
    root2.geometry('800x800')
    root2.config(bg='black')

    
    front = PhotoImage(file='front.png')
    images = [
        PhotoImage(file='thor.png'), PhotoImage(file='vision.png'), PhotoImage(file='witch.png'),
        PhotoImage(file='spiderman.png'), PhotoImage(file='ironman.png'), PhotoImage(file='captain america.png'),
        PhotoImage(file='black panther.png'), PhotoImage(file='groot.png')
    ]
    images = images * 2  
    random.shuffle(images)

    
    flipped_buttons = []
    matched_pairs = 0

    
    buttons = []
    for i in range(len(images)):
        button = tk.Button(root2, image=front, bg='black')
        button.grid(row=i//4+2, column=i%4+1)
        button.image = images[i]  
        button.config(command=lambda b=button, img=images[i]: change_image(b, img))
        buttons.append(button)

    
    def check_match():
        nonlocal matched_pairs
        if len(flipped_buttons) == 2:
            btn1, img1 = flipped_buttons[0]
            btn2, img2 = flipped_buttons[1]
            if img1 == img2:
                matched_pairs += 1
                flipped_buttons.clear()
                if matched_pairs == len(images) // 2:
                    play_succes()
                    messagebox.showinfo("Congratulations", "You've matched all pairs!")
            else:
                root2.after(1000, lambda: [btn1.config(image=front), btn2.config(image=front)])
                flipped_buttons.clear()

    
    def change_image(button, img):
        if button.cget('image') == str(front):
            button.config(image=img)
            flipped_buttons.append((button, img))
            check_match()

    root2.mainloop()

def temp_text(e):
    textbox.delete(0, "end")

def click2():
    tk.Label(root, text='Welcome' + ' ' + textbox.get(), font=('gabriola', 20), bg='black', fg='#40E0D0').place(x=690, y=520)

tk.Label(root, image=bg2).place(x=0, y=0)

textbox = tk.Entry(root, bg="magenta", font=('gabriola', 18), width=50, borderwidth=3)
textbox.insert(0, 'Enter your name')

button = tk.Button(root, image=playkey, command=lambda: [play_but(), secondslide()], borderwidth=10, bg='magenta')
bon = tk.Button(root, text='OK', bg='magenta', font=('arial', 18), command=click2).place(x=1010, y=455)
textbox.place(x=560, y=450)
textbox.bind("<FocusIn>", temp_text)
button.place(x=700, y=600)

play_screen()
root.mainloop()
