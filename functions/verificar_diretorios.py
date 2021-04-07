from os.path import exists
from os import mkdir


def verifica_dirs():
    """
    Essa função é executada no momento da inicialização durante a barra de progresso, para verificar a existência dos di
    retórios necessários para salvar os arquivos PDF's. Caso algum dele ou deles não existam, os mesmos serão criados.
    :return: None
    """
    outputs_directory = r"C:\outputs"
    joined_directory = r"C:\outputs\arquivos-concatenados"
    splitted_dir = r"C:\outputs\arquivos-separados"

    if exists(outputs_directory) is False:
        mkdir(outputs_directory)
        mkdir(joined_directory)
        mkdir(splitted_dir)
        return None

    if exists(joined_directory) is False:
        mkdir(joined_directory)

    if exists(splitted_dir) is False:
        mkdir(splitted_dir)

    return None
