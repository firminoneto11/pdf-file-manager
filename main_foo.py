from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import sleep
from functions.geometria_centralizada import centralizar_janela
from functions.verificar_diretorios import verifica_dirs


def progresso(pb, lab):
    """
    Essa função realiza a inserção na tela da barra de progresso e animação da mesma.
    :param pb: Objeto do tipo Progressbar
    :param lab: Objeto do tipo Label
    :return: None
    """
    for _ in range(100):
        pb['value'] = pb['value'] + 1
        lab.config(text=f"{pb['value']}%")
        pb.update_idletasks()
        sleep(0.015)


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
        janela_raiz.configure(background='#7E52A0')
        janela_raiz.resizable(False, False)
        centralizar_janela(width=1000, height=500, element=janela_raiz)

        # Verificando os diretórios
        verifica_dirs()

        # Criando os widgets que irão apresentar uma barra de carregamento
        status_do_carregamento = Label(janela_raiz, text='0%', font=('Helvetica', 14), bg='#7E52A0', fg='#eeeeee')

        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("aqua.Horizontal.TProgressbar", foreground='white', background='aqua')
        progress_bar = ttk.Progressbar(janela_raiz, style="aqua.Horizontal.TProgressbar", orient=HORIZONTAL, length=500,
                                       mode='determinate')

        loading = Label(janela_raiz, text='Carregando...', font=('Helvetica', 14), bg='#7E52A0', fg='#eeeeee')

        status_do_carregamento.place(x=480, y=300)
        progress_bar.place(x=250, y=250)
        loading.place(x=250, y=200)

        progresso(pb=progress_bar, lab=status_do_carregamento)

        if progress_bar['value'] == 100:
            progress_bar.destroy()
            status_do_carregamento.destroy()
            loading.destroy()
            Label(janela_raiz, text='Carregado!', font=('Helvetica', 16), bg='#7E52A0', fg='#eeeeee').pack(pady=100)

        # Mainloop da aplicação
        janela_raiz.mainloop()

    except Exception as error:
        messagebox.showerror("Problema na inicialização", f"Houve um problema na hora de inicializar o software.\n"
                                                          f"Detalhes do erro: {error}\n"
                                                          f"Pressione 'OK' para finalizar o programa.")
