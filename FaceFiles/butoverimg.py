import tkinter as tk
from PIL import Image,ImageTk
filename = 'face.jpg'
root = tk.Tk()
canvas = tk.Canvas(root,width=740,height=370)
canvas.pack()
tk_img = ImageTk.PhotoImage(file=filename)
canvas.create_image(250,200,image=tk_img)
quit_button = tk.Button(root,text="Quit",command=root.quit,anchor='w',width=10,activebackground="#33B5E5")
quit_button_window = canvas.create_window(600,350,anchor='nw',window=quit_button)
root.mainloop()