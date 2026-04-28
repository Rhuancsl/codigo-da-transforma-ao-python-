class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} [{status}]"

class Biblioteca:
    def __init__(self):
        self.livros = [] 
    

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo_procurado):
        for livro in self.livros:
            if livro.titulo == titulo_procurado:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Empréstimo de '{livro.titulo}' realizado!")
                else:
                    print(f"O livro '{livro.titulo}' já está ocupado.")
                return
        print("Livro não encontrado no acervo.")


biblioteca_municipal = Biblioteca()
l1 = Livro("Noites Brancas", "fyodor dostoevsky")
l2 = Livro("O ego é seu inimigo", "Ryan Holiday")
l3 = Livro("Os segredos da mente milionária", "T. Harv Eker")
l4 = Livro("It a coisa", "Stephen King")

biblioteca_municipal.adicionar_livro(l1)
biblioteca_municipal.adicionar_livro(l2)
biblioteca_municipal.adicionar_livro(l3)
print(l2) 
biblioteca_municipal.emprestar_livro("O Principezinho")
print(l2) 