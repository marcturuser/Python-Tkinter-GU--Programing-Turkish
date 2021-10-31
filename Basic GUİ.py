import tkinter as tk
window=tk.Tk()
window.geometry("1080x1080")
window.wm_title("My App")
window.iconbitmap("worry-cat.ico")# eğer kodu açtıysanız lütfen dosya içindeki worry cat.ico dosyasını da indirin
#ve yol olarak gösterin örnek window.iconbitmap(r"C:\Users\metin\Desktop\PetImages\cat.ico " gibi
window.resizable(False, False)
header = tk.Label(window, text =" HELLO WORLD" ,fg="black",font ="Arial 20")
header.pack()
window.mainloop()