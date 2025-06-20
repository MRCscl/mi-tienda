import tkinter as tk 
from view.login_view import cargar_login  

ventana = tk.Tk()
ventana.title("Mi Tienda")
ventana.geometry("1200x700")

cargar_login(ventana)

ventana.mainloop()