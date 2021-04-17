"""
A cor '#29274C' está fora da paleta de cores, mas é um tom de azul que caiu bem com a tonalidade do projeto.
"""
from tkinter import *
from interfaces.concatenar_area import ConcatenarGui


class MenuInicial:

    def __init__(self, root):
        """
        Essa classe inicializa o menu inicial logo após o carregamento da barra de progresso.
        :param root: Janela raiz.
        """
        # Colocando a janela principal em um atributo de instância
        self.root = root

        # Criando os widgets iniciais
        self.status_do_sistema = Label(root, text='Selecione uma das opções abaixo 👇', font=('Helvetica', 18),
                                       bg='#624CAB', fg='#eeeeee')

        self.concatenar = Button(root, text='Concatenar', width=20, bg='#29274C', fg='#eeeeee', relief='flat',
                                 font=('Helvetica', 12), padx=5, pady=5, borderwidth=2, activebackground='#7189FF',
                                 command=self.__concatenar)
        self.separar = Button(root, text='Separar', width=20, bg='#29274C', fg='#eeeeee', relief='flat',
                              font=('Helvetica', 12), padx=5, pady=5, borderwidth=2, activebackground='#7189FF')

        self.sair = Button(root, text='Sair', width=20, bg='#29274C', fg='#eeeeee', relief='flat',
                           font=('Helvetica', 12), padx=5, pady=5, borderwidth=2, activebackground='#7189FF',
                           command=self.root.quit)

        # Inserindo os elementos na tela
        self.status_do_sistema.place(x=250, y=150)

        self.concatenar.place(x=250, y=250)
        self.separar.place(x=500, y=250)
        self.sair.place(x=375, y=330)

        # Criando os efeitos hovers dos botões
        self.concatenar.bind('<Enter>', self.__1_hover_in)
        self.concatenar.bind('<Leave>', self.__1_hover_out)
        self.separar.bind('<Enter>', self.__2_hover_in)
        self.separar.bind('<Leave>', self.__2_hover_out)
        self.sair.bind('<Enter>', self.__3_hover_in)
        self.sair.bind('<Leave>', self.__3_hover_out)

    def __1_hover_in(self, event):
        self.concatenar.config(bg='#758ECD')

    def __1_hover_out(self, event):
        self.concatenar.config(bg='#29274C')

    def __2_hover_in(self, event):
        self.separar.config(bg='#758ECD')

    def __2_hover_out(self, event):
        self.separar.config(bg='#29274C')

    def __3_hover_in(self, event):
        self.sair.config(bg='#758ECD')

    def __3_hover_out(self, event):
        self.sair.config(bg='#29274C')

    def __concatenar(self):
        """
        Esse método inicializa a classe ConcatenarGui e seus widgets.
        :return: None
        """
        # Removendo os widgets antigos
        self.status_do_sistema.destroy()
        self.concatenar.destroy()
        self.separar.destroy()
        self.sair.destroy()

        # Inicializando a classe
        ConcatenarGui(root=self.root)
