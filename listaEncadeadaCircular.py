from membro import *

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None
        self.apontador = None
    
    def is_empty(self):
        return self.head == None
    
    def adicionar_membro(self, membro : Membro):
        if self.is_empty(): 
            self.head = membro
            membro.setNext(self.head)
            self.apontador = self.head
            return
        valorAtual = self.head.getNext()
        while valorAtual.getNext() != self.head:
            valorAtual = valorAtual.getNext()
        membro.setNext(self.head)
        valorAtual.setNext(membro)
    
    def proximo_responsavel(self):
        if self.is_empty():
            return None
        self.apontador = self.apontador.getNext()
        return self.apontador
    
    def remover_membro(self, membro : str):
        atual = self.head
        ultimo = None
        proximo = atual.getNext()
        if membro == self.head.getNome():
            if self.head == self.head.getNext():
                self.head = None
            else:
                self.head = self.head.getNext()
            return membro
        while atual.getNome() != membro:
            if proximo == self.head:
                return "Elemento não encontrado"
            ultimo = atual
            atual = proximo
            proximo = atual.getNext()
        ultimo.setNext(proximo)
        return atual
    def mostrarLista(self):
        atual = self.head
        while True:
            proximo = atual.getNext()
            if proximo == self.head:
                print(f"{atual} -> (volta para {self.head})")
                return
            print(f"{atual} -> ", end="")
            atual = proximo
            