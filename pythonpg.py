from tkinter import *
root=Tk()
Label(root,text="hello codeworked").pack()
Button(root,text="exit",command=lambda:root.destroy()).pack()

root.title("my application")
root.geometry("400x400")
root.mainloop()