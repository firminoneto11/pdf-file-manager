from tkinter import *


class ConcatenarGui:
    """
    Classe que irá apresentar a GUI da área de concatenação.
    """
    # Atributos das labels e da listbox
    conteudo_status_do_sys = {'text': 'Concatenação', 'font': ('Helvetica', 18), 'bg': '#624CAB', 'fg': '#eeeeee'}
    conteudo_pdf_list = {'bg': '#758ECD', 'width': 125, 'fg': '#eeeeee', 'relief': RIDGE, 'borderwidth': 3}
    conteudo_label_da_dica = {'text': 'Insira arquivos no formato PDF na lista abaixo para realizar a concatenação.',
                              'font': ('Helvetica', 14), 'bg': '#624CAB', 'fg': '#eeeeee'}

    # Atributos dos botões
    conteudo_concatenar = {'text': 'Concatenar', 'font': ('Helvetica', 12), 'width': 25, 'bg': 'green', 'fg': 'white',
                           'relief': FLAT, 'state': DISABLED}
    conteudo_del = {'text': 'Remover Arquivo', 'font': ('Helvetica', 12), 'width': 25, 'bg': 'red', 'fg': 'white',
                    'relief': FLAT, 'state': DISABLED}
    conteudo_add = {'text': 'Adicionar Arquivo', 'font': ('Helvetica', 12), 'width': 25, 'bg': '#A0DDFF', 'fg': 'black',
                    'relief': FLAT}
    conteudo_sair = {'text': 'Voltar ao menu principal', 'font': ('Helvetica', 12), 'width': 25, 'bg': '#29274C',
                     'fg': 'white', 'relief': FLAT}

    def __init__(self, root):
        # Salvando a janela principal em um atributo de instância
        self.root = root

        # Criando os widgets
        self.status_do_sys = Label(self.root, **ConcatenarGui.conteudo_status_do_sys)
        self.label_da_dica = Label(self.root, **ConcatenarGui.conteudo_label_da_dica)

        self.listbox_frame = Frame(self.root)
        self.scroll = Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.pdf_list = Listbox(self.listbox_frame, **ConcatenarGui.conteudo_pdf_list, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.pdf_list.yview)

        self.frame_dos_botoes = Frame(self.root, bg='#624CAB')
        self.concatenar = Button(self.frame_dos_botoes, **ConcatenarGui.conteudo_concatenar)
        self.add_arquivo = Button(self.frame_dos_botoes, **ConcatenarGui.conteudo_add)
        self.del_arquivo = Button(self.frame_dos_botoes, **ConcatenarGui.conteudo_del)
        self.sair = Button(self.frame_dos_botoes, **ConcatenarGui.conteudo_sair)

        # Inserindo os widgets na janela principal
        self.status_do_sys.pack(pady=30)
        self.label_da_dica.pack()

        self.listbox_frame.pack(pady=20)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.pdf_list.pack()

        self.frame_dos_botoes.pack(pady=10)
        self.concatenar.grid(row=0, column=0, padx=3)
        self.add_arquivo.grid(row=0, column=1, padx=3)
        self.del_arquivo.grid(row=0, column=2, padx=3)
        self.sair.grid(row=1, column=1, pady=10)
