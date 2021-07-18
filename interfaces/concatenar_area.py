from tkinter import *
from tkinter import filedialog


class ConcatenarGui:
    """
    Classe que irá apresentar a GUI da área de concatenação.
    """
    # Atributos das labels e da listbox
    conteudo_status_do_sys = {'text': 'Concatenação', 'font': ('Helvetica', 18), 'bg': '#624CAB', 'fg': '#eeeeee'}
    conteudo_pdf_list = {'bg': '#758ECD', 'width': 125, 'fg': '#eeeeee', 'relief': RIDGE, 'borderwidth': 3,
                         'font': ('Helvetica', 12)}
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

    def __init__(self, root, menu_inicial):
        # Salvando a janela principal e o menu inicial em um atributo de instância
        self.root = root
        self.menu_inicial = menu_inicial

        # Criando os widgets
        self.status_do_sys = Label(self.root, **self.conteudo_status_do_sys)
        self.label_da_dica = Label(self.root, **self.conteudo_label_da_dica)

        self.listbox_frame = Frame(self.root)
        self.scroll = Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.pdf_list = Listbox(self.listbox_frame, **self.conteudo_pdf_list, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.pdf_list.yview)

        self.frame_dos_botoes = Frame(self.root, bg='#624CAB')
        self.concatenar = Button(self.frame_dos_botoes, **self.conteudo_concatenar)
        self.add_arquivo = Button(self.frame_dos_botoes, **self.conteudo_add, command=self.adicionar_arquivo)
        self.del_arquivo = Button(self.frame_dos_botoes, **self.conteudo_del, command=self.deletar_arquivo)
        self.sair = Button(self.frame_dos_botoes, **self.conteudo_sair, command=self.__sair)

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

        # Vinculando a função callback alter state para o Widget Listbox
        self.pdf_list.bind("<<ListboxSelect>>", self.__alter_state)

    def __sair(self):
        # Tirando os widgets antigos
        self.status_do_sys.destroy()
        self.label_da_dica.destroy()
        self.listbox_frame.destroy()
        self.frame_dos_botoes.destroy()

        # Voltando ao menu inicial
        self.menu_inicial.__init__(root=self.root)

    def __alter_state(self, event):
        if self.pdf_list.size() > 0:
            self.del_arquivo.config(state=NORMAL)
        else:
            self.del_arquivo.config(state=DISABLED)

        if self.pdf_list.size() >= 2:
            self.concatenar.config(state=NORMAL)
        else:
            self.concatenar.config(state=DISABLED)

    def adicionar_arquivo(self):
        pdf_file = filedialog.askopenfilename(
            initialdir="C:\\",
            title="Escolha um arquivo PDF",
            filetypes=(('Arquivos PDF', '.pdf'), )
        )
        if len(pdf_file) != 0:
            self.pdf_list.insert(END, pdf_file)

        if self.pdf_list.size() >= 2:
            self.concatenar.config(state=NORMAL)
        else:
            self.concatenar.config(state=DISABLED)

    def deletar_arquivo(self):
        self.pdf_list.delete(ANCHOR)
        self.__alter_state(0)
