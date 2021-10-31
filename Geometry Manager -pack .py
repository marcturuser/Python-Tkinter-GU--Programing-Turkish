#klasik kodlarımız
import tkinter as tk
window = tk.Tk()
window.geometry("1080x1080")
window.title ("MY APP")

redbutton = tk.Button(window, text="Red", fg="red") #buton tanımladık
redbutton.pack( side = tk.LEFT, fill= tk.Y, )
greenbutton = tk.Button(window, text="Green", fg="green")#buton tanımladık
greenbutton.pack( side = tk.TOP, fill=tk.X, )
bluebutton = tk.Button(window, text="Blue", fg="blue")#buton tanımladık
bluebutton.pack( side = tk.RIGHT, fill= tk.Y )
blackbutton = tk.Button(window, text="Black", fg="black")#buton tanımladık
blackbutton.pack( side = tk.BOTTOM, fill= tk.X)
pinkbutton = tk.Button(window, text="Purple", fg="purple")#buton tanımladık
pinkbutton.pack( anchor = tk.CENTER,padx = 40 ,pady=40, ipadx= 500 , ipady=500 )


window.mainloop()