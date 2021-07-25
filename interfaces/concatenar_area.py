from tkinter import *
from tkinter import ttk, filedialog, messagebox
from functions.geometria_centralizada import TopLevelNew
from engine.concat import Merger
from os import listdir
import webbrowser


class ConcatenarGui:
    """
    Classe que irá apresentar a GUI da área de concatenação.
    """
    # Atributos das labels e da listbox
    conteudo_status_do_sys = {'text': 'Concatenação', 'font': ('Helvetica', 18), 'bg': '#624CAB', 'fg': '#eeeeee'}
    conteudo_pdf_list = {'bg': '#758ECD', 'width': 125, 'fg': '#eeeeee', 'relief': FLAT, 'borderwidth': 3,
                         'font': ('Helvetica', 10)}
    conteudo_label_da_dica = {'text': 'Insira arquivos no formato PDF na lista abaixo para realizar a concatenação.\n'
                                      'Eles serão agrupados na ordem em que forem inseridos.',
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
        self.concatenar = Button(self.frame_dos_botoes, **self.conteudo_concatenar, command=self.__concatenar)
        self.add_arquivo = Button(self.frame_dos_botoes, **self.conteudo_add, command=self.__adicionar_arquivo)
        self.del_arquivo = Button(self.frame_dos_botoes, **self.conteudo_del, command=self.__deletar_arquivo)
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

    def __alter_state(self, _event):
        """
        Esse método servirá como uma função callback para o evento 'ListboxSelect'. Toda vez que o evento ocorrer, esse
        método é acionado, alterando o estado do botão 'Remover arquivo', sempre garantindo que ele está disponível ape
        nas quando um elemento for selecionado.
        :param _event: ListboxSelect event
        :return: None
        """
        if self.pdf_list.size() > 0:
            self.del_arquivo.config(state=NORMAL)
        else:
            self.del_arquivo.config(state=DISABLED)

    def __checa_tamanho(self):
        """
        Esse método controla o estado do botão 'concatenar', baseado na quantidade de elementos que estão atualmente na
        lista, sempre garantindo que ele estará disponível quando houver 2 ou mais elementos à serem concatenados.
        :return: None
        """
        if self.pdf_list.size() >= 2:
            self.concatenar.config(state=NORMAL)
        else:
            self.concatenar.config(state=DISABLED)

    def __adicionar_arquivo(self):
        """
        Esse método irá adicionar na lista um novo arquivo no formato '.pdf'
        :return: None
        """
        pdf_file = filedialog.askopenfilename(
            initialdir="C:\\",
            title="Escolha um arquivo PDF",
            filetypes=(('Arquivos PDF', '.pdf'), )
        )
        if len(pdf_file) != 0:
            self.pdf_list.insert(END, pdf_file)

        self.__checa_tamanho()

    def __deletar_arquivo(self):
        """
        Esse método irá remover da lista o elemento que está selecionado.
        :return: None
        """
        self.pdf_list.delete(self.pdf_list.curselection())
        self.del_arquivo.config(state=DISABLED)
        self.__checa_tamanho()

    def __concatenar(self):
        files = [file for file in self.pdf_list.get(0, END)]
        AskForNewName(files=files, old_object=self)


class AskForNewName:

    window_title = {'text': 'Insira um nome para o novo arquivo', 'font': ('Helvetica', 18), 'bg': '#624CAB',
                    'fg': '#eeeeee'}
    entry_box = {'width': 50, 'font': ('Helvetica', 14)}
    ok_button = {'text': 'Ok', 'width': 20, 'bg': '#29274C', 'fg': '#eeeeee', 'relief': 'flat',
                 'font': ('Helvetica', 12), 'padx': 5, 'pady': 5, 'borderwidth': 2, 'activebackground': '#7189FF'}
    concat_dir = r'C:\outputs\arquivos-concatenados'

    def __init__(self, files, old_object):

        # Criando a janela para receber o novo nome
        self.new_name_window = TopLevelNew()

        # Aplicando configurações à janela
        self.new_name_window.title("PDF file manager by Firmino Neto")
        self.new_name_window.iconbitmap(r".\icon.ico")
        self.new_name_window.configure(background='#624CAB')
        self.new_name_window.resizable(False, False)
        self.new_name_window.center(width=600, height=250)
        self.new_name_window.grab_set()

        # Lista dos arquivos pdf's selecionados e criação de um atributo de instância que refere à antiga janela
        self.files = files
        self.old_object = old_object
        try:
            self.old_object.pdf_list.selection_clear(self.old_object.pdf_list.curselection())
        except Exception:
            self.old_object.pdf_list.selection_clear(ANCHOR)
        self.old_object.del_arquivo.config(state=DISABLED)

        # Widgets da nova janela
        self.title = Label(self.new_name_window, **self.window_title)
        self.name = ttk.Entry(self.new_name_window, **self.entry_box)
        self.ok = Button(self.new_name_window, **self.ok_button, command=self.concatenate)

        # Captando o 'focus' para o Entry Widget
        self.name.focus_set()

        # Inserindo os widgets na nova janela
        self.title.pack(pady=30)
        self.name.pack(pady=15)
        self.ok.pack(pady=15)

        # Vinculando a função callback para animação hover
        self.ok.bind('<Enter>', self.__hover_in)
        self.ok.bind('<Leave>', self.__hover_out)

        # Vinculando a função callback para o botão 'enter'
        self.new_name_window.bind('<Return>', self.concatenate)

    def __hover_in(self, _event):
        self.ok.config(bg='#758ECD')

    def __hover_out(self, _event):
        self.ok.config(bg='#29274C')

    def concatenate(self, _event=None):
        self.old_object.del_arquivo.config(state=DISABLED)
        name = self.name.get()
        if len(name) == 0:
            self.new_name_window.destroy()
            messagebox.showinfo(
                title="Nome inválido",
                message="O nome não pode estar em branco."
            )
        elif name + '.pdf' in listdir(self.concat_dir):
            self.new_name_window.destroy()
            messagebox.showinfo(
                title="Nome inválido",
                message="O novo nome para o arquivo já existe."
            )
        else:
            try:
                name = name + '.pdf'
                Merger.merge(files=self.files, new_name=name)
            except Exception as error:
                # Excluindo a nova janela de nome
                self.new_name_window.destroy()

                # Mostrando uma menssagem de erro após a exceção ser lançada
                messagebox.showerror(
                    title="Erro na operação",
                    message=f"Houve um erro no momento da concatenação. Mais detalhes:\n{error}"
                )
            else:
                # Limpando a lista dos arquivos pdf's e alterando o estado do botão
                self.old_object.pdf_list.delete(0, END)
                self.old_object.concatenar.config(state=DISABLED)

                # Excluindo a nova janela de nome
                self.new_name_window.destroy()

                # Mostrando uma menssagem de sucesso após a concatenação
                messagebox.showinfo(
                    title="Arquivos concatenados",
                    message=f"Os arquivos foram concatenados com sucesso. O novo arquivo se encontra disponível "
                            f"em:\n{self.concat_dir}"
                )

                # Abrindo o diretório dos arquivos concatenados
                webbrowser.open(self.concat_dir)
            finally:
                # Liberando a antiga janela para ser clicada
                self.new_name_window.grab_release()
