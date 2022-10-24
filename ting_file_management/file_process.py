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
    if len(instance) < 1:
        sys.stdout.write("Não há elementos\n")
        return
    removendo_arquivo = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {removendo_arquivo} removido com sucesso\n")
    return


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
        return
    except IndexError:
        sys.stderr.write(str("Posição inválida\n"))
