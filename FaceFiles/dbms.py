import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.geometry("500x500")
path = 'C:\\Users\\MY PC\\Desktop\\face recog.jpg'
imagefile = ImageTk.PhotoImage(Image.open(path))
label = Label(root,image = imagefile)
canvas = tk.Canvas(root,width=1000,height=1000)
canvas.pack()
tk_img = ImageTk.PhotoImage(file = path)
canvas.create_image(2000,2000,image=tk_img)
button = tk.Button(root,text="Quit",command =root.quit,anchor='w',width=10,activebackground="#33B5E5" )
button_window=canvas.create_window(10,10,anchor='nw',window=button)
label.pack()
root.mainloop()