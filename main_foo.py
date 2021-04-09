from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import sleep
from functions.geometria_centralizada import centralizar_janela
from functions.verificar_diretorios import verifica_dirs
from interfaces.main_menu_gui import MenuInicial


def main():
    """
    Essa é função principal do programa que deve ser executada.
    :return: None
    """
    try:
        # Criando a janela principal
        janela_raiz = Tk()

        # Aplicando configurações a janela
        janela_raiz.title("PDF file manager by Firmino Neto")
        janela_raiz.iconbitmap(r".\icon.ico")
        janela_raiz.configure(background='#624CAB')
        janela_raiz.resizable(False, False)
        centralizar_janela(width=1000, height=500, element=janela_raiz)

        # Verificando os diretórios
        verifica_dirs()

        # Criando os widgets que irão apresentar uma barra de carregamento
        status_do_carregamento = Label(janela_raiz, text='0%', font=('Helvetica', 14), bg='#624CAB', fg='#eeeeee')

        estilo = ttk.Style()
        estilo.theme_use('alt')
        estilo.configure("aqua.Horizontal.TProgressbar", background='aqua')

        progress_bar = ttk.Progressbar(janela_raiz, style="aqua.Horizontal.TProgressbar", orient=HORIZONTAL, length=500,
                                       mode='determinate')

        loading = Label(janela_raiz, text='', font=('Helvetica', 16), bg='#624CAB', fg='#eeeeee')

        status_do_carregamento.place(x=480, y=300)
        progress_bar.place(x=250, y=250)
        loading.place(x=250, y=200)

        # Loop 'for' para efetuar o carregamento da barra de progresso
        for _ in range(100):
            if progress_bar['value'] >= 0 and (progress_bar['value'] < 50):
                loading.config(text='Carregando...')
            else:
                loading.config(text='Checando diretórios...')

            progress_bar['value'] = progress_bar['value'] + 1
            status_do_carregamento.config(text=f"{progress_bar['value']}%")
            progress_bar.update_idletasks()
            sleep(0.020)

        # Após a execução da função que realiza o carregamento da barra de progresso, os widgets são removidos e o menu
        # inicial é apresentado
        progress_bar.destroy()
        status_do_carregamento.destroy()
        loading.destroy()

        # Inicializando a classe MenuInicial
        MenuInicial(root=janela_raiz)

        # Mainloop da aplicação
        janela_raiz.mainloop()

    except Exception as error:
        messagebox.showerror("Problema na inicialização", f"Houve um problema na hora de inicializar o software.\n"
                                                          f"Detalhes do erro: {error}\n"
                                                          f"Pressione 'OK' para finalizar o programa.")
