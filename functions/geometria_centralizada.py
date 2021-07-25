from tkinter import Tk, Toplevel


def centralizar_janela(width, height, element):
    screen_width, screen_height = element.winfo_screenwidth(), element.winfo_screenheight()
    pos_x = screen_width / 2 - width / 2
    pos_y = screen_height / 2 - height / 2
    element.geometry("%dx%d+%d+%d" % (width, height, pos_x, pos_y))


class TkinterNew(Tk):

    def center(self, width, height):
        """
        Essa função centraliza uma widget janela de acordo com o tamanho da tela na qual ela é apresentada.
        :param width: Largura desejada para a janela.
        :param height: Altura desejada para a janela.
        :return: None
        """
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        pos_x = screen_width / 2 - width / 2
        pos_y = screen_height / 2 - height / 2
        self.geometry("%dx%d+%d+%d" % (width, height, pos_x, pos_y))


class TopLevelNew(Toplevel):
    def center(self, width, height):
        """
        Essa função centraliza uma widget janela de acordo com o tamanho da tela na qual ela é apresentada.
        :param width: Largura desejada para a janela.
        :param height: Altura desejada para a janela.
        :return: None
        """
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        pos_x = screen_width / 2 - width / 2
        pos_y = screen_height / 2 - height / 2
        self.geometry("%dx%d+%d+%d" % (width, height, pos_x, pos_y))
