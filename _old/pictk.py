from tkinter import *
window = Tk()
window.geometry("1255x944")
photo = PhotoImage(file="/home/ansh/Desktop/python_experiments/1.png")
label = Label(image=photo)
label.pack()
window.mainloop()