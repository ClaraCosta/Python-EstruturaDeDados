#Codifique uma classe denominada ListaEncadeada e uma classe denominada No atendendo aos seguintes requisitos

#A classe No deve possuir duas propriedades: carga e prox, sendo carga um valor de qualquer tipo e prox uma referência para o próximo nó do encadeamento.

#A classe ListaEncadeada deve ter duas propriedades: cabeca e cauda, que apontam respectivamente para os nós (i.e., instâncias da classe No) que iniciam e terminam a lista encadeada.

'''''A classe ListaEncadeada deve ter os seguintes métodos:
- inserir_no_inicio(valor): insere um valor no início da lista
- inserir_no_final(valor): insere um valor no final da lista
- remover_do_inicio(): remove o elemento do início da lista
- remover_do_final(): remove o elemento do final da lista
- __str__(): exibe todos os itens itens da lista'''''

#A classe nó deve ter um método __str__() que exiba a sua carga


class No:
    def __init__(self, carga: object = None, prox: 'No' = None):
        self.carga = carga
        self.prox = prox

    def __str__(self) -> str:
        return str(self.carga)

class ListaEncadeada:
    def __init__(self):
        self.cabeca: 'No' = None
        self.cauda: 'No' = None

    def inserir_valor_no_inicio(self, valor: object):
        novo:'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo # Se a lista está vazia, o novo elemento é referenciado tanto como cabeca, como cauda

        else: #Caso a cabeça ou cauda não estejam vazias
            novo.prox = self.cabeca #Será adicionada uma nova cabeça
            self.cabeca = novo

    def imprimir_lista(self):
        if self.cabeca is None:
            print("Lista Vazia")
            return
        atual: 'No' = self.cabeca
        while atual is not None:
            print(str(atual.carga) + " ")
            atual = atual.prox
            
    def inserir_valor_no_final(self, valor):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo # Se a lista está vazia, o novo elemento é referenciado tanto como cabeca, como cauda
        else:
            self.cauda.prox = novo
            self.cauda = novo 

    def remover_do_inicio(self):
      if self.cabeca is None:
          print("Lista vazia")
          return
      
      if self.cabeca == self.cauda: #Se a lista possuir apenas um elemento, e ele for removido, a lista ficará vazia.
          self.cabeca = self.cauda = None

      else:
          self.cabeca = self.cabeca.prox #O próximo elemento inserido será a cabeça

    def remover_do_final(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            atual: 'No' = self.cabeca
            while atual.prox is not self.cauda:
                atual = atual.prox

            self.cauda = atual
            atual.prox = None


lista = ListaEncadeada()
lista.inserir_valor_no_inicio(8)
lista.inserir_valor_no_inicio(4)
lista.inserir_valor_no_inicio(7)
lista.inserir_valor_no_inicio(1)
lista.inserir_valor_no_inicio(5)
lista.imprimir_lista()
lista.remover_do_final()
print("depois de remover do final")
lista.imprimir_lista()
lista.remover_do_inicio()
print("depois de remover do inicio")
lista.imprimir_lista()
