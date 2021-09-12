#-------------------------------------------------------------------------------
#          Name: Login
#
#         Autor: Marco Contreras
#
# Código fuente: https:github.com/enidev911
#     Copyright: (c) Marco Contreras
#       Licence: <your licence>
#-------------------------------------------------------------------------------


from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ast

w=Tk()
width_window = 925
height_window = 500
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_window/2)
y_coordinate = (screen_height/2)-(height_window/2)
w.geometry("%dx%d+%d+%d"%(width_window, height_window, x_coordinate, y_coordinate))


def signin():
    '''
    Función que nos permitirá mostrar los widget par
    el formulario para iniciar sesión
    '''
    signin_win=Frame(w, width=925, height=500, bg='white')
    signin_win.place(x=0, y=0)
    f1=Frame(signin_win, width=350, height=350, bg='white')
    f1.place(x=480, y=100)

    global img1
    img1 = ImageTk.PhotoImage(Image.open("signin.png"))
    Label(signin_win, image=img1, border=0, bg='white').place(x=50,y=50)

    l2=Label(signin_win,text="Sign in",fg='#ff4f5a',bg='white')
    l2.config(font=('Microsoft YaHei UI Light',23, 'bold'))
    l2.place(x=600,y=60)

    #---------------|input usuario|------------------------------
    def on_enter(e):
        e1.delete(0,'end')
    def on_leave(e):
        if e1.get()=='':
            e1.insert(0,'Usuario')

    e1 =Entry(f1,width=25,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',11, ))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'Usuario')
    e1.place(x=30,y=60)
    #Línea para identificar el entry usuario
    Frame(f1,width=295,height=2,bg='black').place(x=25,y=87)
    #------------------------------------------------------

    #----------------|input password|---------------------------
    def on_enter(e):
        e2.delete(0,'end')
    def on_leave(e):
        if e2.get()=='':
            e2.insert(0,'Contraseña')

    e2 =Entry(f1,width=21,fg='black',border=0,bg='white')
    e2.config(font=('Microsoft YaHei UI Light',11, ))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0,'Contraseña')
    e2.place(x=30,y=130)
    #Línea para identificar el entry password
    Frame(f1,width=295,height=2,bg='black').place(x=25,y=157)
    #------------------------------------------------------

    # mecanismo ------------------------------------------------
    def signin_cmd():

        file=open('datausers.txt','r')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()


        key=e1.get()
        value=e2.get()

        if key in r.keys() and value==r[key]:
            messagebox.showinfo("","Inicio de sesión correcto")
            w.destroy()
            import main
        else:
            messagebox.showwarning('Re-intentar', 'Usuario o contraseña invalido')

    #------------------------------------------------------
    Button(f1,width=39,pady=7,text='Iniciar sesión',bg='#ff4f5a',fg='white',border=0,command=signin_cmd).place(x=35,y=204)
    l1=Label(f1,text="¿No tienes una cuenta?",fg="black",bg='white')
    l1.config(font=('Microsoft YaHei UI Light',9, ))
    l1.place(x=75,y=250)
    b2=Button(f1,width=7,text='Registrate',border=0,bg='white',fg='#ff4f5a',command=signup)
    b2.place(x=215,y=250)



def signup():
    '''
    Función que nos permitirá mostrar los widget
    para el formulario para registrarse
    '''
    signup_win = Frame(w, width=925, height=500, bg='white')
    signup_win.place(x=0, y=0)
    f1=Frame(signup_win, width=350, height=350, bg='white')
    f1.place(x=480, y=70)

    global img2
    img2 = ImageTk.PhotoImage(Image.open('signup.png'))
    Label(signup_win, image=img2, border=0, bg='white').place(x=30, y=90)

    l2=Label(signup_win, text='Registrarse', fg='#ff4f5a', bg='white')
    l2.config(font=('Microsoft YaHei Ui Light', 23, 'bold'))
    l2.place(x=600,y=60)


    #---------------|input usuario|-----------------------------
    def on_enter(e=None):
        e1.delete(0, 'end')
    def on_leave(e):
        if e1.get()=='':
            e1.insert(0,'Usuario')

    e1=Entry(f1, width=25, fg='black', border=0, bg='white')
    e1.config(font=('Microsoft YaHei Ui Light', 11,))
    # Eventos (bind)
    e1.bind("<FocusIn>",on_enter)
    e1.bind("<FocusOut>",on_leave)
    e1.insert(0,'Usuario')
    e1.place(x=30, y=60)
    # La línea que identifica al Entry Usuario
    Frame(f1, width=295, height=2, bg='black').place(x=25, y=87)
    #-----------------------------------------------------------

    #---------------|input password|-----------------------------
    def on_enter(e=None):
        e2.delete(0, 'end')
    def on_leave(e=None):
        if e2.get()=='':
            e2.insert(0,'Contraseña')

    e2 = Entry(f1, width=21, fg='black', border=0, bg='white')
    e2.config(font=('Microsoft YaHei UI Light',11, ))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("FocusOut", on_leave)
    e2.insert(0, 'Contraseña')
    e2.place(x=30, y=130)
    # La línea que identifica al Entry Contraseña
    Frame(f1, width=295, height=2, bg='black').place(x=25, y=157)
    #-----------------------------------------------------------


    #---------------|input confirmar password|-------------------
    def on_enter(e=None):
        e2.delete(0, 'end')
    def on_leave(e=None):
        if e2.get()=='':
            e2.insert(0,'Confirmar contraseña')

    e3 = Entry(f1, width=21, fg='black', border=0, bg='white')
    e3.config(font=('Microsoft YaHei UI Light',11, ))
    e3.bind("<FocusIn>", on_enter)
    e3.bind("<FocusOut>", on_leave)
    e3.insert(0, 'Confirmar contraseña')
    e3.place(x=30, y=130+70)
    # La línea que identifica al Entry Confirmar contraseña
    Frame(f1, width=295, height=2, bg='black').place(x=25, y=157+70)
    #-----------------------------------------------------------

    # Mecanismo
    def signup_cmd():
        key=e1.get()
        value=e2.get()
        value2=e2.get()

        if value==value2:
            file=open('datausers.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)
            print(r)


            dict2={key:value}
            print(dict2)
            r.update(dict2)
            print(r)
            file.truncate(0)
            file.close()
            print(r)
            file=open('datausers.txt', 'w')
            w=file.write(str(r))

            messagebox.showinfo("","Registro exitoso")

        else:
            messagebox.showinfo("Re-intentar", "La contraseña no es la misma")

        # ===================================================================

    Button(f1, width=39, pady=7, text='Registrarse', bg='#ff4f5a',fg='white',
            border=0, command=signup_cmd).place(x=35, y=204+60)


    l1=Label(f1,text="¿Ya tienes una cuenta?",fg="black",bg='white')
    l1.config(font=('Microsoft YaHei UI Light',9, ))
    l1.place(x=70,y=250+63)

    b2=Button(f1,width=6,text='Inicia sesión',border=0,bg='white',fg='#ff4f5a',command=signin)
    b2.place(x=210,y=250+63)






signin() # Pantalla por defecto

w.mainloop()