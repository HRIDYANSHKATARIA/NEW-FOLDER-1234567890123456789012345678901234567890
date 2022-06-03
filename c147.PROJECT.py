from tkinter import *

root = Tk()
root.title("ASCII NUMBERS")
root.geometry("400x400")
root.configure(background='snow')
  
enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.5,anchor=CENTER)

label = Label(root,text="NAME IN ASCII - ",bg="light yellow",fg="black")
label2 = Label(root,text="ENCRPYTED - ",bg="light yellow",fg="black")

def asciiconverter():
    input_word = enter_word.get()
    ascii = str(ord(letter))
    encrypted = ascii - 1
    for letter in input_word:
        label["text"]+=str(ord(letter)) +" "
        
    for encrypted in input_word:
        label2["text"]+=str(chr(encrypted)) +" "
        
btn = Button(root,text="SHOW NAME IN ASCII",command=asciiconverter,bg='gold',fg='black')
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)
label2.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()