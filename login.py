import tkinter
from tkinter import *

class login:
     def __init__(self, master=None):
         self.janela = Frame(master)
         self.fontePadrao = ("Arial","12")
         self.janela.pack()
         self.titulo = Label(self.janela,text= "informe os dados")
         self.titulo["font"] = ("Arial","29","bold")
         self.titulo.pack()

         self.janela2 = Frame(master)
         self.janela2["padx"] = 20
         self.janela2.pack()

         self.janela3 = Frame(master)
         self.janela3["padx"] = 20
         self.janela3.pack()

         self.janela4 = Frame(master)
         self.janela4["padx"] = 20
         self.janela4.pack()

         self.janela5 = Frame(master)
         self.janela5["padx"] = 20
         self.janela5.pack()

         self.janela6 = Frame(master)
         self.janela6["padx"] = 20
         self.janela6.pack()

         self.janela7 = Frame(master)
         self.janela7["padx"] = 20
         self.janela7.pack()

         self.janela8= Frame(master)
         self.janela8["padx"] = 20
         self.janela8.pack()

         self.nomeLabel = Label(self.janela2,text="idusuario",font=self.fontePadrao)
         self.nomeLabel.pack(side=LEFT)
         self.nome = Entry(self.janela2)
         self.nome["width"] = 30
         self.nome["font"] = self.fontePadrao
         self.nome.pack(side=LEFT)

         self.autenticar = Button(self.janela2)
         self.autenticar["text"] = "buscar"
         self.autenticar["font"] = ("Calibri", "8")
         self.autenticar["width"] = 12
         self.autenticar["command"] = self.verificarSenha
         self.autenticar.pack()

         self.senhaLabel = Label(self.janela3, text="nome", font=self.fontePadrao)
         self.senhaLabel.pack(side=LEFT)
         self.senha = Entry(self.janela3)
         self.senha["width"] = 30
         self.senha["font"] = self.fontePadrao
         self.senha["show"] = "*"
         self.senha.pack(side=LEFT)

         self.senhaLabel = Label(self.janela4, text="telefone", font=self.fontePadrao)
         self.senhaLabel.pack(side=LEFT)
         self.senha = Entry(self.janela4)
         self.senha["width"] = 30
         self.senha["font"] = self.fontePadrao
         self.senha["show"] = "*"
         self.senha.pack(side=LEFT)

         self.senhaLabel = Label(self.janela5, text="E-MAIL", font=self.fontePadrao)
         self.senhaLabel.pack(side=LEFT)
         self.senha = Entry(self.janela5)
         self.senha["width"] = 30
         self.senha["font"] = self.fontePadrao
         self.senha["show"] = "*"
         self.senha.pack(side=LEFT)

         self.senhaLabel = Label(self.janela6, text="usúario", font=self.fontePadrao)
         self.senhaLabel.pack(side=LEFT)
         self.senha = Entry(self.janela6)
         self.senha["width"] = 30
         self.senha["font"] = self.fontePadrao
         self.senha["show"] = "*"
         self.senha.pack(side=LEFT)

         self.senhaLabel = Label(self.janela7, text="senha", font=self.fontePadrao)
         self.senhaLabel.pack(side=LEFT)
         self.senha = Entry(self.janela7)
         self.senha["width"] = 30
         self.senha["font"] = self.fontePadrao
         self.senha["show"] = "*"
         self.senha.pack(side=LEFT)

         self.autenticar = Button(self.janela8)
         self.autenticar["text"] = "usuario"
         self.autenticar["font"] = ("Calibri", "8")
         self.autenticar["width"] = 12
         self.autenticar["command"] = self.verificarSenha
         self.autenticar.pack()

         self.autenticar = Button(self.janela8)
         self.autenticar["text"] = "cidades"
         self.autenticar["font"] = ("Calibri", "8")
         self.autenticar["width"] = 12
         self.autenticar["command"] = self.verificarSenha
         self.autenticar.pack()

         self.autenticar = Button(self.janela8)
         self.autenticar["text"] = "clientes"
         self.autenticar["font"] = ("Calibri", "8")
         self.autenticar["width"] = 12
         self.autenticar["command"] = self.verificarSenha
         self.autenticar.pack()

         self.autenticar = Button(self.janela8)
         self.autenticar["text"] = "fechar"
         self.autenticar["font"] = ("Calibri", "8")
         self.autenticar["width"] = 12
         self.autenticar["command"] = self.verificarSenha
         self.autenticar.pack(side=LEFT)

         self.mensagem = Label(self.janela4, text = "", font = self.fontePadrao)
         self.mensagem.pack()

     def verificarSenha(self):
        usuario = self.nome.get()
        senha  = self.senha.get()
        if usuario == "usuarioSenai" and senha == "123456":
           self.mensagem["text"] = "autenticado"
        else:
           self.mensagem["text"] = "Erro na autenticacao"

root = Tk()
login(root)
root.mainloop()