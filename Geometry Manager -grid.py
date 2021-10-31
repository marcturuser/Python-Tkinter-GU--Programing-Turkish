import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.geometry("700x300")
window.title ("Sıgn Up")
#labellarımız
""" Öncelikle labellarımızı ekleyelim ve çalışmamızda nasıl duracak bir bakalım."""
l_header= tk.Label(window, text="Register My Application",fg= "black",
                   font= "arial 12")
l_header.grid(row= 0,column=2,pady=20)
""" senin için yukarıdaki çizimde column ve rowları belirttim. Sadece hepsini yerleştirme
ile uğraşacağız"""
l_name= tk.Label(window , text= "Name", fg= "black", font= "arial 12")
l_name.grid(row=1, column =0,  )
l_surname=tk.Label(window , text= "Surname", fg= "black", font= "arial 12")
l_surname.grid(row=2, column =0)
l_birthdate=tk.Label(window , text= "BirthDate", fg= "black", font= "arial 12")
l_birthdate.grid(row=3, column =0)
l_email=tk.Label(window , text= "E-mail", fg= "black", font= "arial 12")
l_email.grid(row=4)
"""#neden burada bunu yazdın derseniz default yani sıfır olan değerleri 
yazmak sadece kod kalabalığı yapar burada değerimiz sıfır olduğu için
yazmamıza gerek yoktu ama ben sizin için yazdım"""
""" ooo entryler spinboxlar comboboxlar falan neler oluyor derseniz bunları şimdilik göz
ardı edebilirsiniz odaklanmamız gereken noktalar yerleştirme """
#entrylerimiz
e_name= tk.Entry( fg= "black", font= "arial 12")
e_name.grid(row=1, column =1, )
e_surname= tk.Entry( fg= "black", font= "arial 12")
e_surname.grid(row=2, column =1,)
e_email= tk.Entry( fg= "black", font= "arial 12")
e_email.grid(row=4, column =1,)
#spinboxlarımız
sp_date=tk.Spinbox(window,from_=0, to=30, wrap= True)
sp_date.grid(row=3, column =1, ipadx=24, ipady= 1)
sp_year= tk.Spinbox(window, from_= 1800 , to= 2021, wrap = True)
sp_year.grid(row=3, column =3,ipady= 1)

""" bu arada daha çok fonksiyon işlevlere göre sıralanabilir ve yazılabilir tutorialları
incelerseniz göreceksiniz. 2. yazımda bu fonksiyonlara değineceğim. Proje için gerekli
 arayüzü ve sizin için bir adet değişik bir arayüzü paylaşacağım """
#comboboxımız
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
month_cb = ttk.Combobox(window)
month_cb['values'] = months
month_cb['state'] = 'readonly'  # normal
month_cb.grid(row=3, column =2,  ipadx=13 )
#butonlarımız
b_signup=tk.Button(window, text="Sign Up", fg= "white", bg="green")
b_signup.grid(row=5, column =2,ipadx=30, pady= 10)
b_signin=tk.Button(window, text="Sign In", fg= "white", bg="green")
b_signin.grid(row=6, column =2,ipadx=30, )
l_acc=tk.Label(window , text= "You have account? Sign In", fg= "black",
               font= "arial 10", pady=15)
l_acc.grid(row=6,column=1)
window.mainloop()