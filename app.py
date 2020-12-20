from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator

#create tk window
root = Tk()
root.title('Google KMA')
root.geometry("500x600")
#root.iconbitmap(l'ogo.ico')

load=Image.open('bg.jpg')
render=ImageTk.PhotoImage(load)

img=Label(root,image=render)
img.place(x=0,y=0)


name=Label(root,text="ThanhKMA",fg="#FFFFFF",bd=0,bg="#03152D")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)

box=Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate():
    INPUT = box.get(1.0,END)
    #print(INPUT)
    t=Translator()
    a=t.translate(INPUT,src="vi",dest="en")
    b=a.text
    box1.insert(END,b)

clear_button = Button(button_frame,text="Clear text",font=(("Arial"),10,'bold'),bg="#303030",fg="#FFFFFF",command=clear)
clear_button.place(x=150,y=310)

change_button = Button(button_frame,text="Change",font=(("Arial"),10,'bold'),bg="#303030",fg="#FFFFFF",command=translate)
change_button.place(x=290,y=310)

box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)

box2=Text(root,width=28,height=8,font=("ROBOTO",16))
box2.pack(pady=50)


root.mainloop()