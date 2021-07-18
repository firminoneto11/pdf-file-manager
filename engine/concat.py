from PyPDF3 import PdfFileMerger
from os.path import join


class Merger:
    """
    Essa classe é uma classe estática que contém os métodos para realizar a operação de concatenação.
    """

    # Output directory
    concat_dir = r'C:\outputs\arquivos-concatenados'

    @staticmethod
    def merge(files, new_name):
        """
        Esse método adiciona cada arquivo pdf já tratado na classe PdfFileMerger importada do módulo PyPDF3, classe es
        ta que ficará responsável pelo processo de concatenação.
        :param files: Lista/array contendo os arquivos que foram selecionados pelo usuário.
        :param new_name: Novo nome para o arquivo que foi escolhido pelo usuário
        :return: None
        """
        paths = list(map(Merger.toPath, files))
        merger = PdfFileMerger()
        for path in paths:
            merger.append(path)
        merger.write(join(Merger.concat_dir, new_name))
        merger.close()

    @staticmethod
    def toPath(file_string):
        """
        Esse método faz o tratamento do 'path' dos arquivos, pois no windows é necessário utilizar 'double backslash' pa
        ra representar paths no sistema operacional.
        :param file_string: String antiga representando o caminho até o arquivo.
        :return: Nova string contendo o path ajustado para windows.
        """
        path = file_string.split('/')
        return '\\'.join(path)
