def exists_word(word, instance):
    for fileira in range(instance.__len__()):
        arquivo = instance.search(fileira)
        lista_ocorrencia = []
        i = 1
        for fileira, linha in enumerate(arquivo["linhas_do_arquivo"]):
            if word.lower() in linha.lower():
                lista_ocorrencia.append({"linha": i})
            i += 1
        lista_de_palavras = []
        resultado = {}
        total_ocorrencia = len(lista_ocorrencia)
        if total_ocorrencia > 0:
            resultado["palavra"] = word
            resultado["arquivo"] = arquivo["nome_do_arquivo"]
            resultado["ocorrencias"] = lista_ocorrencia
            lista_de_palavras.append(resultado)
    return lista_de_palavras


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
