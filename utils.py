import json

def carregar_dados(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def encontrar_registro(lista, codigo):
    for item in lista:
        if item['codigo'] == codigo:
            return item
    return None

def incluir_registro(lista, caminho, campos):
    try:
        codigo = int(input("Informe o código: "))
        if encontrar_registro(lista, codigo):
            print("Código já existente.")
            return
        registro = {"codigo": codigo}
        for campo in campos:
            registro[campo] = input(f"Informe {campo}: ")
        lista.append(registro)
        salvar_dados(caminho, lista)
        print("Registro incluído com sucesso!")
    except ValueError:
        print("Código inválido.")

def listar_registros(lista, titulo):
    print(f"\nLISTA DE {titulo.upper()}")
    if lista:
        for item in lista:
            print(" - ", item)
    else:
        print("Nenhum registro encontrado.")

def atualizar_registro(lista, caminho, campos):
    try:
        codigo = int(input("Informe o código a atualizar: "))
        registro = encontrar_registro(lista, codigo)
        if registro:
            for campo in campos:
                registro[campo] = input(f"Novo {campo} ({registro[campo]}): ") or registro[campo]
            salvar_dados(caminho, lista)
            print("Registro atualizado com sucesso!")
        else:
            print("Registro não encontrado.")
    except ValueError:
        print("Código inválido.")

def excluir_registro(lista, caminho):
    try:
        codigo = int(input("Informe o código a excluir: "))
        registro = encontrar_registro(lista, codigo)
        if registro:
            lista.remove(registro)
            salvar_dados(caminho, lista)
            print("Registro excluído com sucesso!")
        else:
            print("Registro não encontrado.")
    except ValueError:
        print("Código inválido.")