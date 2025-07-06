from utils import *

caminho = "data/disciplinas.json"
campos = ["nome"]

def menu_disciplinas():
    lista = carregar_dados(caminho)
    while True:
        print("\n--- MENU DISCIPLINAS ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("9. Voltar")
        opcao = input("Escolha: ")
        if opcao == "1":
            incluir_registro(lista, caminho, campos)
        elif opcao == "2":
            listar_registros(lista, "disciplinas")
        elif opcao == "3":
            atualizar_registro(lista, caminho, campos)
        elif opcao == "4":
            excluir_registro(lista, caminho)
        elif opcao == "9":
            break
        else:
            print("Opção inválida.")