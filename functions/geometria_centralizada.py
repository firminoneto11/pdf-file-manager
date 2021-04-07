

def centralizar_janela(width, height, element):
    """
    Essa função centraliza uma widget janela de acordo com o tamanho da tela na qual ela é apresentada.
    :param width: Largura desejada para a janela
    :param height: Altura desejada para a janela
    :param element: A própria janela (Objeto do tipo Tk)
    :return: None
    """
    screen_width, screen_height = element.winfo_screenwidth(), element.winfo_screenheight()
    posx, posy = screen_width / 2 - width / 2, screen_height / 2 - height / 2
    element.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
