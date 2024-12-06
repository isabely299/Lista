# Programa para gerenciar uma lista
def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Sair")

def adicionar_item(lista):
    item = input("Digite o item para adicionar: ")
    lista.append(item)
    print(f'"{item}" foi adicionado à lista.')

def remover_item(lista):
    item = input("Digite o item para remover: ")
    if item in lista:
        lista.remove(item)
        print(f'"{item}" foi removido da lista.')
    else:
        print(f'"{item}" não está na lista.')

def exibir_lista(lista):
    if lista:
        print("\nItens na lista:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    else:
        print("\nA lista está vazia.")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_item(lista)
        elif opcao == "2":
            remover_item(lista)
        elif opcao == "3":
            exibir_lista(lista)
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
