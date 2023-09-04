import Produto

class CarrinhoDeCompras():
    def __init__(self, produtos: str) -> None:
        self.produtos = produtos
        
    
    def inserir_produto(self,produto: str) -> None:
        self.listProduto = []
        self.listProduto = produto
        
    
    def lista_produto(self) -> None:
        for i in self.listProduto:
            print(i.nome, i.valor)
    
    
    def soma_total(self):
        valor = 0
        for produto in self.listProduto:
            valor += self.listProduto.valor
        
        return valor        