class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivamente(self.raiz, valor)
            
    def _inserir_recursivamente(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivamente(no_atual.esquerda, valor)
        
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            
            else:
                self._inserir_recursivamente(no_atual.direita, valor)
                
    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor) 
    
    def _buscar_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        if valor < no_atual.valor:
            return self._buscar_recursivamente(no_atual.esquerda, valor)
        return self._buscar_recursivamente(no_atual.direita, valor)
    
    def altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, no_atual):
        if no_atual is None:
            return 0
        altura_esquerda = self._calcular_altura(no_atual.esquerda)
        altura_direita = self._calcular_altura(no_atual.direita)
        return max(altura_esquerda, altura_direita) + 1

    def nos_internos(self):
        return self._contar_nos_internos(self.raiz)

    def _contar_nos_internos(self, no_atual):
        if no_atual is None:
            return 0
        if no_atual.esquerda or no_atual.direita:
            return 1 + self._contar_nos_internos(no_atual.esquerda) + self._contar_nos_internos(no_atual.direita)
        return 0
    def folhas(self):
        return self._contar_folhas(self.raiz)

    def _contar_folhas(self, no_atual):
        if no_atual is None:
            return 0
        if not no_atual.esquerda and not no_atual.direita:
            return 1
        return self._contar_folhas(no_atual.esquerda) + self._contar_folhas(no_atual.direita)


# Exemplo de uso:
if __name__ == "__main__":
    arvore = ArvoreBinaria()
    numeros = [8, 9, 10, 2, 12 ,13, 14, 20]

    for numero in numeros:
        arvore.inserir(numero)

    print("\nÁrvore Binária")
    print("\nRaiz:", arvore.raiz.valor)
    print("\nAltura:", arvore.altura())
    print("\nNós Internos:", arvore.nos_internos())
    print("\nFolhas:", arvore.folhas())
    

    numero_busca = 4
    if arvore.buscar(numero_busca):
        print(f"\n{numero_busca} está presente na árvore.")
    else:
        print(f"\n{numero_busca} não está presente na árvore.")

    print("\nNúmeros:", numeros,"\n")