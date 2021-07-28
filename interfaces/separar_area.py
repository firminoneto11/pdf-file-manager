from tkinter import *


class SepararGui:
    status = {
        'text': 'Separação',
        'font': ('Helvetica', 18),
        'bg': '#624CAB',
        'fg': '#eeeeee'
    }

    dica = {
        'text': 'Selecione um arquivo para separá-lo, página por página.',
        'font': ('Helvetica', 14),
        'bg': '#624CAB',
        'fg': '#eeeeee'
    }

    botao_voltar = {
        'text': 'Voltar ao menu principal',
        'font': ('Helvetica', 12),
        'width': 25,
        'bg': '#29274C',
        'fg': 'white',
        'relief': FLAT
    }

    def __init__(self, root, menu_inicial):
        # Salvando a janela principal e o menu inicial em um atributo de instância
        self.root = root
        self.menu_inicial = menu_inicial

        # Widgets
        self.status_do_sys = Label(self.root, **self.status)
        self.label_da_dica = Label(self.root, **self.dica)

        self.voltar = Button(self.root, **self.botao_voltar, command=self.__sair)

        # Colocando os widgets na tela
        self.status_do_sys.pack(pady=30)
        self.label_da_dica.pack()

        self.voltar.pack(pady=30)

    def __sair(self):
        # Tirando os widgets antigos
        self.status_do_sys.destroy()
        self.label_da_dica.destroy()
        self.voltar.destroy()

        # Voltando ao menu inicial
        self.menu_inicial.__init__(root=self.root)
