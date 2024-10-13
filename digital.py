from tkinter import Label,Tk

import time

appWindow=Tk()
appWindow.title("Dijital Saat")
appWindow.geometry("400x200")
appWindow.resizable(0,0)
appWindow.configure(bg="black")

textFont =("Boulder",36,'bold')
background="black"
foreground="white"
border_width=20

#saat etiketi
label=Label(appWindow,font=textFont,bg=background,fg=foreground)
label.grid(row=0,column=1,padx=10,pady=10)
#tarih etiketi
dateLabel=Label(appWindow,font=textFont,bg=background,fg=foreground)
dateLabel.grid(row=1,column=1,padx=10,pady=10)

def digitalClock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    dateİnfo=time.strftime("%d %B %Y")
    dateLabel.config(text=dateİnfo)
    label.after(200,digitalClock)
digitalClock()
appWindow.mainloop()