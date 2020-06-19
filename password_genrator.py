from tkinter import *
import random
wn=Tk()
wn.geometry("600x300")
wn.title("Password Genrator")
wn.configure(bg="white")

def generate():
    characters="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!@#$%^&*_:;"
    password_list=random.sample(characters, int(password_length_entry.get()))
    password="".join(password_list)
    get_password_entry.delete(0, END)
    get_password_entry.insert(END, password)

frame1=Frame(wn, bg="white")
frame1.pack(side=TOP)

password_length_label=Label(frame1, text="Length of Password :: ", font=("consolas 25"), bg="white")
password_length_label.pack(side=LEFT)

password_length_entry=Entry(frame1, bd=2.5, font=("consolas"))
password_length_entry.pack(side=LEFT)
password_length_entry.focus()

password_button=Button(wn, text="Genrate", font=("consolas"), command=generate)
password_button.pack(side=TOP)

password_frame=Frame(wn, bg="white")
password_frame.pack(side=TOP)

password_label=Label(password_frame, text="Password :: ", font=("consolas 25"), bg="white")
password_label.pack(side=LEFT)

get_password_entry=Entry(password_frame, bd=2.5, font=("consolas"))
get_password_entry.pack(side=LEFT)

wn.bind("<Return>", lambda pressed_kay:generate())

wn.mainloop()

