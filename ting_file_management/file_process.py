import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for fileira in instance._data:
        if fileira["nome_do_arquivo"] == path_file:
            return
    texto = txt_importer(path_file)
    objeto = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(texto),
        "linhas_do_arquivo": texto
    }
    instance.enqueue(objeto)
    sys.stdout.write(str(objeto))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
