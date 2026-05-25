#Exercicio 25
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

#exercicio 27
    def exibir_informacoes(self):
        # Exemplo de formatação monetária básica usando LaTeX: R$ Preço
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")


#exercicio 26
meu_produto = Produto(nome="Notebook Gamer", preco=4500.00)

# Chamando o método para exibir as informações
meu_produto.exibir_informacoes()                                                                                 