from tkinter import *
import time

master = Tk()
master.title("Portal do aluno 2023")
master.geometry("490x560+610+153")
master.iconbitmap(default="icones\\ico.ico")
master.resizable(width=1,height=1)


#Funções
def nova_janela():
    master1 = Tk()
    master1.title("Nova Janela Criada!")
    master1.geometry("490x560+610+153")

    time.sleep(0.3)
    master.destroy()

#VARIAVEIS GLOBAIS
esconda_senha = StringVar()


#IMPORTAR IMAGENS
img_fundo = PhotoImage(file="imagens\\Fundo.png")
img_botao = PhotoImage(file="imagens\\ENTRAR.png")


#Criação de labels
lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

#Criação de caixa de entrada
en_token = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_token.place(width=378, height=58,x=64, y=126)

en_email = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_email.place(width=378, height=58, x=64, y=250)

en_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
en_senha.place(width=378, height=58,x=64, y=362)

#Criação de botões
bt_entrar = Button(master, bd=0, image= img_botao, command=nova_janela)
bt_entrar.place(width=274, height=73,x=79, y=457)

master.mainloop()
