"""
Aprendiendo Python ejercicio Calculadora con formulario:
    - 2 campos de texto
    - 4 botones para las operaciones
    - Capturar excepción si usuario mete letras
    - Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox

ventana= Tk()
ventana.title("Ej. Calculadora")
ventana.geometry("250x225")
ventana.resizable(0,0)

num1 = IntVar()
num2 = IntVar()

def alerta(resultado):
    MessageBox.showinfo("Resultado",resultado)


def sumar():
    try:
        resultado = num1.get() + num2.get()
        alerta("El resultado de la suma es: " + str(resultado))
    except:
        MessageBox.showerror("Error","Introduce los datos correctos!!")

def resta():
    try:
        resultado = num1.get() - num2.get()
        alerta("El resultado de la resta es: " + str(resultado))
    except:
        MessageBox.showerror("Error","Introduce los datos correctos!!")

def multiplicacion():
    try:
        resultado = num1.get() * num2.get()
        alerta("El resultado de la suma es: " + str(resultado))
    except:
        MessageBox.showerror("Error","Introduce los datos correctos!!")

def division():
    try:
        resultado = num1.get() / num2.get()
        alerta("El resultado de la suma es: " + str(resultado))
    except:
        MessageBox.showerror("Error","Introduce los datos correctos!!")

def borrar():
    num1.set(0)
    num2.set(0)    

Label(ventana).grid(row=0,column=0)
Label(ventana, text="Numero 1: ",width=10).grid(row=1,column=0,padx= 10, pady=5)
Label(ventana, text="Numero 2: ",width=10).grid(row=2,column=0,padx= 5, pady=5)

Entry(ventana, textvariable=num1, width=20,justify=CENTER).grid(row=1,column=1,columnspan=3 ,padx= 5, pady=5)
Entry(ventana, textvariable=num2, width=20,justify=CENTER).grid(row=2,column=1,columnspan=3,padx= 5, pady=5)

Label(ventana).grid(row=3,column=0)
Button(ventana, text="Sumar",command= sumar,width=15).grid(row=4,column=0,columnspan=2,padx= 5, pady=5)
Button(ventana, text="Resta",command= resta,width=15).grid(row=4,column=2,columnspan=2,padx= 5, pady=5)

Button(ventana, text="Multiplicación",command= multiplicacion ,width=15).grid(row=5,column=0,columnspan=2,padx= 5, pady=5)
Button(ventana, text="División",command= division ,width=15).grid(row=5,column=2,columnspan=2,padx= 5, pady=5)

Button(ventana, text="Borrar",command= borrar ,width=15).grid(row=6,column=0,columnspan=4,padx= 5, pady=5)
ventana.mainloop()