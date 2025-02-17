from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1 = text
    sec1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=sec1,dest=dest1)
    return trans1.text

def data():
    s = com_sor.get()
    d = com_dest.get()
    masg = sor_txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root=Tk()

root.title("Google Translator")
root.geometry("500x700")
root.config(bg="Red")

lab_txt = Label(root,text="Translator",font=("Arial",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

sor_txt = Label(root,text="Source Text",font=("Arial",20,"bold"),fg="black",bg="red")
sor_txt.place(x=100,y=100,height=20,width=300)

sor_txt = Text(frame,font=("Arial",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())

com_sor = ttk.Combobox(frame,values=list_text)
com_sor.place(x=10,y=300,height=40,width=150)
com_sor.set("From")

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

com_dest = ttk.Combobox(frame,values=list_text)
com_dest.place(x=330,y=300,height=40,width=150)
com_dest.set("To")

dest_txt = Label(root,text="Destination Text",font=("Arial",20,"bold"),fg="black",bg="red")
dest_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Arial",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()
