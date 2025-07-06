from estudantes import menu_estudantes
from professores import menu_professores
from disciplinas import menu_disciplinas
from turmas import menu_turmas
from matriculas import menu_matriculas

def menu_principal():
    while True:
        print("\n=== SISTEMA DE GESTÃO ACADÊMICA ===")
        print("1. Estudantes")
        print("2. Professores")
        print("3. Disciplinas")
        print("4. Turmas")
        print("5. Matrículas")
        print("9. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            menu_estudantes()
        elif opcao == "2":
            menu_professores()
        elif opcao == "3":
            menu_disciplinas()
        elif opcao == "4":
            menu_turmas()
        elif opcao == "5":
            menu_matriculas()
        elif opcao == "9":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
