15. Crie uma agenda no terminal com dicionários que permita adicionar, buscar, listar e remover contatos.
R:
agenda = {}
while True:
    op = input("[1]Add [2]Buscar [3]Listar [4]Remover [5]Sair: ")
    if op == "1":
        agenda[input("Nome: ")] = input("Telefone: ")
    elif op == "2":
        print(agenda.get(input("Nome: "), "Não encontrado"))
    elif op == "3":
        for k, v in agenda.items(): print(f"{k}: {v}")
    elif op == "4":
        agenda.pop(input("Nome: "), None)
    elif op == "5":
        break
