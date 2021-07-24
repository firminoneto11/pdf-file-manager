from PyPDF3 import PdfFileReader, PdfFileWriter
from os import listdir, remove
from os.path import join, isdir
import shutil as sh
from engine.concat import Merger


class Splitter:
    """
    Essa classe é uma classe estática que contém os métodos para realizar a operação de separação.
    """

    # Output directory
    splitter_dir = r'C:\outputs\arquivos-separados'

    @staticmethod
    def split(file):
        """
        Esse método irá separar página por página do arquivo que o usuário escolher e as salvar no 'output directory'
        como novos arquivos pdf. Cada arquivo corresponderá à uma página do documento original.
        :param file: O arquivo escolhido pelo usuário para fazer a separação das páginas
        :return: None
        """
        # Limpando o diretório para evitar duplicidade em arquivos/diretórios
        Splitter.cleanDir()

        # Tratando o nome do arquivo
        file = Merger.toPath(file)

        # Lógica para separação das páginas dos arquivos PDF's e nova nomeclatura para os mesmos
        with open(file, mode='rb') as pdf_file_to_read:
            file_length = PdfFileReader(pdf_file_to_read).numPages

            for page in range(file_length):
                pdf_file = PdfFileReader(pdf_file_to_read)
                current_page = PdfFileWriter()
                current_page.addPage(pdf_file.getPage(page))
                with open(join(Splitter.splitter_dir, f"página_{page + 1}.pdf"), mode='wb') as pdf:
                    current_page.write(pdf)

    @staticmethod
    def cleanDir():
        """
        Esse método irá remover todos os arquivos e diretórios que existam dentro da pasta de destino dos arquivos sepa
        rados, para que os novos arquivos sejam criados corretamente, prevenindo erros.
        """
        for element in listdir(Splitter.splitter_dir):
            current_element = join(Splitter.splitter_dir, element)
            if isdir(current_element):
                sh.rmtree(current_element)
            else:
                remove(current_element)
