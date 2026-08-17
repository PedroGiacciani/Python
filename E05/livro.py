from datetime import date

class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("Titulo é obrigatório!")

        if not autor:
            raise ValueError("Autor é obrigatório")

        if ano < 1450 or ano > date.today().year:
            raise ValueError("Ano inválido")
        
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self):
        return(f"{self.titulo} - {self.autor} ({self.ano})")

    def idade(self):
        return date.today().year - self.ano

    def classico(self):
        if livro.idade() > 100:
            return("É clássico")
        else:
            return("Não é clássico")

livro = Livro("Romeu e Julieta", "Shakespeare", 1591)
# print(livro.descricao())
# print(livro.idade())

acervo = [
    Livro("Romeu e Julieta", "Shakespeare", 1591),
    Livro("A Arte da Guerra", "Sun Tzu", 1450),
    Livro("Biblia Sagrada", "Jesus Cristo", 1450),
    Livro("It - A coisa", "Stephen King", 1980)
]

# for livro in acervo:
#     print(f"{livro.titulo} - {livro.autor} ({livro.ano})")

if __name__ == "__main__":
    acervo = [
        Livro("Romeu e Julieta", "Shakespeare", 1591),
        Livro("A Arte da Guerra", "Sun Tzu", 1450)
    ]

    for livro in acervo:
        print(f"{livro.descricao()} - {livro.idade()} anos, {livro.classico()}")

    #Livro("Teste", "alguem", 3000)
