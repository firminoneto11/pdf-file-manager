from tkinter import *
from tkinter import ttk, filedialog, messagebox
from engine.spliter import Splitter
import webbrowser


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

    master_frame = {
        'bg': '#624CAB',
        'fg': '#eeeeee',
        'padx': 200,
        'pady': 30
    }

    choose_a_file = {
        'text': 'Escolha um arquivo: ',
        'font': ('Helvetica', 14),
        'bg': '#624CAB',
        'fg': '#eeeeee'
    }

    choose_a_file_button = {
        'text': 'Novo arquivo',
        'font': ('helvetica', 12),
        'width': 20,
        'bg': '#012A36',
        'fg': '#eeeeee',
        'relief': FLAT,
        'padx': 5,
        'pady': 5,
        'borderwidth': 2,
        'activebackground': '#7189FF'
    }

    chosen_file = {
        'text': '',
        'font': ('Helvetica', 14),
        'state': 'readonly',
        'width': 50
    }

    separate_button = {
        'text': 'Separar',
        'state': DISABLED,
        'bg': 'green',
        'fg': '#eeeeee',
        'width': 20,
        'padx': 5,
        'pady': 5,
        'relief': FLAT
    }

    botao_voltar = {
        'text': 'Voltar ao menu principal',
        'font': ('Helvetica', 12),
        'width': 25,
        'bg': '#29274C',
        'fg': 'white',
        'relief': FLAT,
        'padx': 5,
        'pady': 5,
        'borderwidth': 2,
        'activebackground': '#7189FF'
    }

    splitter_dir = r'C:\outputs\arquivos-separados'

    def __init__(self, root, menu_inicial):
        # Salvando a janela principal e o menu inicial em um atributo de instância
        self.root = root
        self.menu_inicial = menu_inicial

        # Widgets
        self.status_do_sys = Label(self.root, **self.status)
        self.label_da_dica = Label(self.root, **self.dica)
        self.main_frame = LabelFrame(self.root, **self.master_frame)

        Label(self.main_frame, **self.choose_a_file).grid(row=0, column=0, padx=5)
        Button(self.main_frame, **self.choose_a_file_button, command=self.__select_file).grid(row=0, column=1, padx=5)
        Label(self.main_frame, bg='#624CAB').grid(row=1, column=0)  # Label only for style purposes
        Label(self.main_frame, bg='#624CAB').grid(row=2, column=0)  # Label only for style purposes
        Label(self.main_frame, bg='#624CAB').grid(row=3, column=0)  # Label only for style purposes
        Label(self.main_frame, bg='#624CAB').grid(row=4, column=0)  # Label only for style purposes
        Label(self.main_frame, bg='#624CAB').grid(row=5, column=0)  # Label only for style purposes
        self.file = ttk.Entry(self.main_frame, **self.chosen_file)
        self.separate = Button(self.main_frame, **self.separate_button, command=self.__split)

        self.voltar = Button(self.root, **self.botao_voltar, command=self.__sair)

        # Colocando os widgets na tela
        self.status_do_sys.pack(pady=30)
        self.label_da_dica.pack()

        self.main_frame.pack(pady=30)
        self.file.place(rely=0.5, x=-80)
        self.separate.place(rely=0.9, x=120)

        self.voltar.pack(pady=30)

        # Configurando as animações hover
        self.voltar.bind('<Enter>', self.__1_hover_in)
        self.voltar.bind('<Leave>', self.__1_hover_out)

    def __1_hover_in(self, _event):
        self.voltar.config(bg='#758ECD')

    def __1_hover_out(self, _event):
        self.voltar.config(bg='#29274C')

    def __sair(self):
        # Tirando os widgets antigos
        self.status_do_sys.destroy()
        self.label_da_dica.destroy()
        self.main_frame.destroy()
        self.voltar.destroy()

        # Voltando ao menu inicial
        self.menu_inicial.__init__(root=self.root)

    def __select_file(self):
        pdf_file = filedialog.askopenfilename(
            initialdir="C:\\",
            title="Escolha um arquivo PDF",
            filetypes=(('Arquivos PDF', '.pdf'),)
        )
        self.file.config(state=ACTIVE)
        self.file.delete(0, END)
        self.file.insert(0, pdf_file)
        self.file.config(state='readonly')
        self.separate.config(state=NORMAL)

    def __split(self):
        file = self.file.get()
        response = messagebox.askyesno(
            title="Atenção",
            message=f"Antes de continuar com a separação em páginas do arquivo escolhido, certifique-se que a seguinte "
                    f"pasta esteja sem arquivos:\n{self.splitter_dir}\nCaso haja algum arquivo, eles serão removidos "
                    f"permanentemente. Deseja continuar?"
        )
        if response:
            try:
                Splitter.split(file)
            except Exception as error:
                messagebox.showerror(
                    title="Erro",
                    message=f"Houve um erro no momento da separação das páginas:\n{error}"
                )
            else:
                messagebox.showinfo(
                    title="Arquivo separado com sucesso",
                    message=f"O arquivo selecionado foi separado com sucesso. A(s) página(s) se encontra(m) em:\n"
                            f"{self.splitter_dir}"
                )
                webbrowser.open(self.splitter_dir)
