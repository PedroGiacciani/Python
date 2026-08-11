acervo = []

op = int(input("Bem vindo! \n1 - Cadastrar Livro\n2 - Procurar\n3 - Listar\n0 - Sair\n"))

while op != 0:
    if op == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano do livro: "))

        acervo.append({"titulo": titulo, "autor": autor, "ano": ano})
        print(f"Livro cadastrado:")
        print(acervo)

        op = int(input("Bem vindo! \n1 - Cadastrar Livro\n2 - Procurar\n3 - Listar\n0 - Sair\n"))
    elif op == 2:
        procurado = input("Digite o Livro que deseja procurar: ")
        encontrado = None

        for livro in acervo:
            if livro["titulo"] == procurado:
                encontrado = livro
                break

        if encontrado:
            print(f"Livro encontrado! {encontrado}")
        else:
            print(f"O livro {procurado} não está no nosso acervo =/")

        op = int(input("Bem vindo! \n1 - Cadastrar Livro\n2 - Procurar\n3 - Listar\n0 - Sair\n"))
    elif op == 3:
        if len(acervo) == 0:
            print("Acervo vazio")
        else:
            for livro in acervo:
                livro.get("ano", "Ano indisponível")
                print(f"{livro["titulo"]} ({livro["ano"]}) - {livro["autor"]}")

        op = int(input("Bem vindo! \n1 - Cadastrar Livro\n2 - Procurar\n3 - Listar\n0 - Sair\n"))
    elif op == 0:
        print("Ok, programa encerrando...")
        break
    else:
        print(f"Por favor, digite um número válido")
        break


#Pergunta 1: O int no input do livro
#Pergunta 2: O int no input do livro
#Pergunta 3: Apenas na parte de cadastrar o livro e listar ele